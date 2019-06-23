from getdb import AccDb
from datetime import datetime
from ui_parts_idea import Ui_partidea
from PyQt5.QtWidgets import QDialog, QTextEdit, QMessageBox, QCheckBox


class IdeaDialog(QDialog, Ui_partidea):
    def __init__(self, parent, _username, department, _unpass_id):
        super().__init__(parent)
        self.ctlname_zh = {'txt_tec_part': '技术部',
                           'txt_pro_part': '工艺部',
                           'txt_qc_part': '质量部',
                           'txt_tec_support': '技术支持部',
                           'txt_general_m': '总经办'}
        self._username = _username
        self.department = department
        self._unpass_id = _unpass_id
        self.parent = parent
        self.setupUi(self)
        self.ctl = self.findChild(QTextEdit, dict(zip(self.ctlname_zh.values(), self.ctlname_zh.keys()))[self.department])
        db = AccDb()
        with db:
            sql = 'select {} from 不合格品登记 where ID={}'.format(
                ','.join([part + '意见' for part in self.ctlname_zh.values()]), _unpass_id
            )
            get_selfpre_sql = 'select 责任自审 from 不合格品登记 where ID=%d' % _unpass_id
            rst = db.get_rst(sql)
            flag_rst = db.get_rst(get_selfpre_sql)
        for i in range(len(rst[0])):
            eval('self.%s.setPlainText(rst[0][i])' % list(self.ctlname_zh.keys())[i])

        start_type_idea_flag = flag_rst[0][0]    # if 责任自审未完成 then 不能输入处理意见
        if not start_type_idea_flag:
            self.setWindowTitle(self.windowTitle() + '>>>当前不合格品处理尚未完成分析、预防及改善办法提交')
        for ctl in self.findChildren(QTextEdit):
            if self.ctlname_zh[ctl.objectName()] == department and start_type_idea_flag:
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
        contents = self.ctl.toPlainText()
        db = AccDb()
        with db:
            sql = "update 不合格品登记 set {}意见='{}' where ID={}".format(self.department, contents, self._unpass_id)
            db.modify_db(sql)
        QMessageBox.information(self, 'Update success', '本次更新完成！')

    def sign(self):
        old_cont = self.ctl.toPlainText()
        sign_info = "\t\t>>>填写人:{}\n\t\t>>>填写日期：{}".format(self._username, datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.ctl.setPlainText(old_cont + '\n' + sign_info)

    def add_methods(self):
        old_cont = self.ctl.toPlainText()
        check_list = self.gpb_deal.findChildren(QCheckBox)
        deal_methods = ','.join([check.text() for check in check_list if check.isChecked()])
        self.ctl.setPlainText("处置方式>>> {}\n{}".format(deal_methods, old_cont))
