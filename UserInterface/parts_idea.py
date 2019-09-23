from getdb import MysqlDb
from sms_wechat import SmsWechat
from report import write2pdf
from datetime import datetime
from ui_parts_idea import Ui_partidea
from PyQt5.QtWidgets import QDialog, QTextEdit, QMessageBox, QCheckBox


class IdeaDialog(QDialog, Ui_partidea):
    def __init__(self, parent, username, department, deal_id):
        super().__init__(parent)
        self.ctl_name_zh = {'txt_tec_part': '技术部',
                            'txt_pro_part': '工艺部',
                            'txt_qc_part': '质量部',
                            'txt_tec_support': '技术支持部'}
        self.username = username
        self.department = department
        self.deal_id = deal_id
        self.parent = parent
        self.setupUi(self)
        self.ctl = self.findChild(QTextEdit,
                                  dict(zip(self.ctl_name_zh.values(), self.ctl_name_zh.keys()))[self.department])
        db = MysqlDb()
        with db:
            sql = 'SELECT {} FROM 不合格品登记 WHERE ID={}'.format(
                ','.join([part + '意见' for part in self.ctl_name_zh.values()]), deal_id
            )
            flag_sql = 'SELECT 责任自审 FROM 不合格品登记 WHERE ID=%d' % deal_id
            rst = db.get_rst(sql)
            flag_rst = db.get_rst(flag_sql)
        for i in range(len(rst[0])):
            eval('self.%s.setPlainText(list(rst[0].values())[i])' % list(self.ctl_name_zh.keys())[i])

        start_type_idea_flag = flag_rst[0]['责任自审']  # if 责任自审未完成 then 不能输入处理意见
        if not start_type_idea_flag:
            self.setWindowTitle(self.windowTitle() + '>>>当前不合格品处理尚未完成分析、预防及改善办法提交')
        for ctl in self.findChildren(QTextEdit):
            if self.ctl_name_zh[ctl.objectName()] == department and start_type_idea_flag:
                ctl.setReadOnly(False)
            else:
                if not start_type_idea_flag:
                    self.btn_deal_method.setEnabled(False)
                    self.btn_sign_name.setEnabled(False)
                    self.btn_save_idea.setEnabled(False)
                ctl.setReadOnly(True)
        self.btn_save_idea.clicked.connect(self.save_idea)
        self.btn_sign_name.clicked.connect(self.sign)
        self.btn_deal_method.clicked.connect(self.add_methods)

    def save_idea(self):
        from mainwindow import FIELDS_IN_TAB3
        contents = self.ctl.toPlainText().strip()
        if contents != '':
            db = MysqlDb()
            with db:
                sql = "UPDATE 不合格品登记 SET {}意见='{}' WHERE ID={}".format(self.department, contents, self.deal_id)
                db.modify_db(sql)

                # start write PDF
                fields = list(FIELDS_IN_TAB3.values())[:5]
                info = []
                fd = ','.join(FIELDS_IN_TAB3.values())
                sql = "SELECT {} FROM 不合格品登记 a INNER JOIN 状态标记 b ON a.ID=b.ID WHERE a.ID={}" \
                      "".format(fd, self.deal_id)
                pre_rst = db.get_rst(sql)
            d = pre_rst[0]
            for k, v in d.items():
                v = '' if v is None else v
                d[k] = str(v)
            for k in fields:
                info.append(d.pop(k))
            write2pdf(fields, info, d)  # write PDF out to output/file_name.pdf

            # start use wechat send message
            batch, _, pro_name, _, _ = info
            filename = pro_name + '-' + batch + '.pdf'
            wechat = SmsWechat()
            wechat.send_message(msg_type='text', contents='{} {}更新不良品评审单(ID={})了,请点击查看!'
                                                          ''.format(self.department, self.username, self.deal_id))
            wechat.send_message(msg_type='file', file_obj=open('output/{}'.format(filename), 'rb'))

            self.parent.fuzzy_search()
            QMessageBox.information(self, 'Update success', '本次更新完成！')

    def sign(self):
        sign_info = "\t>>>{}\n\t>>>{}".format(self.username, datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.ctl.append(sign_info)

    def add_methods(self):
        check_list = self.gpb_deal.findChildren(QCheckBox)
        deal_methods = ','.join([check.text() for check in check_list if check.isChecked()])
        contents = "处置方式>>> {}".format(deal_methods)
        self.ctl.append(contents)
