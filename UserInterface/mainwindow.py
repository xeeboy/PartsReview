# pragma execution_character_set("utf-8")
import user_info

from getdb import *
from ui_mainwindow import *
from ui_part_need_review import *
from ui_about import *
from qa_data import AddDataForm, TEST_ITEMS
from parts_idea import IdeaDialog
from chgpwd import ChgPwd
from chguser import ChgUser
from add_method import AddMethod
from new_unpass import NewUnpass
from plot_item import PlotItem
from report import write2pdf

from xlsxwriter import Workbook
from os.path import join
from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor, QIcon, QBrush, QColor, QPalette
from PyQt5.QtWidgets import QMainWindow, QTableView, QMenu, QAction, QMessageBox, QFileDialog


# on tab1
FIELDS_UNPASS = ['ID', '客户', '批号', '不良品名称', '责任部门', '送部门评审', '技术部意见', '工艺部意见',
                 '质量部意见', '技术支持部意见']

idea = ','.join(("IF(ISNULL({}) or {}='','待输入','已更新')"
                 "".format(part_idea, part_idea) for part_idea in FIELDS_UNPASS[-4:]))

TBL_UNPASS_SQL = "SELECT a.ID,客户,批号,不良品名称,caseto_by_QA,IF(b.b_m_rev=TRUE,'YES','NO'),{} " \
                 "FROM 不合格品登记 a INNER JOIN 状态标记 b ON a.ID=b.ID WHERE b.case_closed_flag=FALSE".format(idea)

FIELDS_IN_TAB1 = {'ID': 'ID', 'batch': '批号', 'prodate': '生产日期', 'unpasstype': '不良品种类',
                  'unpassname': '不良品名称', 'unpassqty': '数量Kg', 'describe': '不合格描述',
                  'result': '原因分析', 'correctiveaciton': '纠正措施', 'precaution': '预防措施',
                  'person': '自审人', 'pre_time': '自审时间', 'pre_check': '责任自审',
                  'parts': 'part_need_review'}

# on tab2
FIELDS_PRE = ['ID', '本部评审', '批号', '不良品名称', '客户', '生产日期', '数量Kg', '不良品种类', 'Review Finish', 'To_General']
FIELDS_IN_TAB2 = {'pre_describle': '不合格描述', 'pre_result': '原因分析',
                  'pre_correctiveation': '纠正措施', 'pre_precaution': '预防措施',
                  'pre_tec_idea': '技术部意见', 'pre_pro_idea': '工艺部意见',
                  'pre_qa_idea': '质量部意见', 'pre_tec_support_idea': '技术支持部意见',
                  'pre_info_purchase': '采购部评审信息', 'pre_info_produce': '生产部评审信息',
                  'pre_info_process': '工艺部评审信息', 'pre_info_logistics': '物流部评审信息',
                  'pre_info_tec': '技术部评审信息', 'pre_info_qa': '质量部评审信息',
                  'pre_info_general': '总经办评审信息', 'lbl_rev_parts_need': 'part_need_review'}
# on tab3
FIELDS_FOLLOW_VIEW = ['ID', 'CaseClosed', '批号', '不良品名称', '数量Kg', '处理次数', '不良剩余Kg', '客户']
FIELDS_IN_TAB3 = {'batch_flw': '批号', 'prodate_flw': '生产日期', 'unpassname_flw': '不良品名称', 'unpassqty_flw': '数量Kg', 'unpasstype_flw': '不良品种类'}
FIELDS_IN_TAB3.update({k+'_flw': v for k, v in FIELDS_IN_TAB2.items()})
FIELDS_IN_TAB3.pop('lbl_rev_parts_need_flw')


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.act_chgpwd.triggered.connect(self.chgpwd)
        self.act_chguser.triggered.connect(self.chguser)
        self.act_about.triggered.connect(self.show_about)

        # set tab0
        self.set_tbl_unpass(TBL_UNPASS_SQL)
        self.show_test_win.clicked.connect(self.test_win)
        self.save_unpass.clicked.connect(self.type_new_unpass)
        self.btn_search.clicked.connect(self.fuzzy_search)
        self.btn_slparts.clicked.connect(self.show_select_parts_frm)
        self.btn_save.clicked.connect(self.save)
        self.tbl_unpass.clicked.connect(self.show_unpass_item)
        self.pre_check.clicked.connect(self.preview)
        self.tbl_unpass.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tbl_unpass.customContextMenuRequested.connect(self.rclick_tbl_unpass)

        # set tab1
        self.pre_tbl_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pre_tbl_view.customContextMenuRequested.connect(self.rclick_tbl_pre)
        self.pre_tbl_view.clicked.connect(self.show_pre_item)  # self.pre_tbl_view.setMouseTracking(True)
        self.btn_sign_pre.clicked.connect(self._pre_sign)

        # set tab2
        self.on_follow_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.on_follow_view.customContextMenuRequested.connect(self.rclick_follow_view)
        self.btn_print.clicked.connect(self.to_pdf)

        # set tab3
        self.test_result_view.setStyleSheet(
            "selection-color: rgb(222, 12, 127);\nselection-background-color: rgb(85, 255, 127);")
        self.test_search.clicked.connect(self.search_test_result)
        self.btn_to_excel.clicked.connect(self.to_excel)
        self.btn_to_spc.clicked.connect(self.show_chart_item)

    def to_pdf(self):
        fields = list(FIELDS_IN_TAB3.values())[:5]
        info = []
        row = self.on_follow_view.currentIndex().row()
        if row != -1:
            unpass_id = int(self.model_on_follow.item(row, 0).text())
            _db = MysqlDb()
            with _db:
                fd = ','.join(FIELDS_IN_TAB3.values())
                sql = "SELECT {} FROM 不合格品登记 a INNER JOIN 状态标记 b ON a.ID=b.ID WHERE a.ID={}" \
                      "".format(fd, unpass_id)
                pre_rst = _db.get_rst(sql)
                d = pre_rst[0]
                for k, v in d.items():
                    v = '' if v is None else v
                    d[k] = str(v)
                for k in fields:
                    info.append(d.pop(k))
            try:
                write2pdf(fields, info, d)
                QMessageBox.information(self, '提示:', '已生成pdf文档至安装目录的output文件夹！')
            except Exception as e:
                user_info.log2txt('生成pdf文档时发生错误：{}'.format(e))
                QMessageBox.information(self, '提示:', '生成pdf文档时发生错误，请查看错误日志！')
        else:
            QMessageBox.warning(self, '未选择', '请先选择项目！')
            pass

    def show_chart_item(self):
        """show chart for items selected"""
        plot_frm = PlotItem(self)
        plot_frm.show()

    def to_excel(self):
        """export to *.xls file"""
        try:
            row_count = self.test_result_model.rowCount()
            col_count = len(self.test_result_fields)
            directory = QFileDialog.getExistingDirectory(self, "选择存放的位置")
            if directory:
                filename = join(directory, 'test_result.xlsx')
                wkb = Workbook(filename)
                sht = wkb.add_worksheet("test_result")
                sht.write_row('A1', self.test_result_fields)
                for r in range(row_count):
                    for c in range(col_count):
                        sht.write(r+1, c, self.test_result_model.item(r, c).text())
                wkb.close()
                QMessageBox.information(self, '完成', '文件地址：{}'.format(filename))
        except Exception as e:
            user_info.log2txt('导出成excel时发生错误：{}'.format(e))
            pass

    def search_test_result(self):
        """method in tab4"""
        keyword = self.test_sch_key.text()
        keyword = '' if keyword is None else keyword
        _pro_info_fields = ('客户', '产品型号', '颜色', '生产日期')
        self.test_result_fields = _pro_info_fields + TEST_ITEMS

        sql = "SELECT {0},a.批号,IF(表面判定=TRUE,'PASS',IF(表面判定 IS NULL,NULL,'UNPASS'))," \
              "IF(RoSH=TRUE,'PASS',IF(RoSH IS NULL,NULL,'UNPASS'))," \
              "{1} FROM 产品信息 a INNER JOIN 常规性能 b ON a.批号=b.批号 " \
              "WHERE CONCAT(客户,产品型号,颜色,b.批号) like '%{2}%'" \
              "".format(','.join(_pro_info_fields), ','.join(TEST_ITEMS[3:]), keyword)

        self.test_result_model = get_model(self.test_result_fields, sql)
        # deal with bigint value use 科学计数
        for i in range(self.test_result_model.rowCount()):
            v = self.test_result_model.item(i, 14).text()
            if v:
                self.test_result_model.setItem(i, 14, QStandardItem('%.2e' % int(v)))
        self.test_result_view.setModel(self.test_result_model)
        self.set_tbl_format('test_result_view')

    def test_win(self):
        frm = AddDataForm(self)
        frm.showMaximized()

    def type_new_unpass(self):
        new_unpass_frm = NewUnpass(self)
        new_unpass_frm.show()

    def chgpwd(self):
        chg_pwd = ChgPwd(self)
        chg_pwd.show()

    def chguser(self):
        chg_user = ChgUser(self)
        chg_user.show()

    def show_about(self):
        about_frm = QDialog(self)
        about_ui = Ui_about()
        about_ui.setupUi(about_frm)
        pe = QPalette()
        pe.setColor(QPalette.Window, Qt.white)  # 设置背景色
        about_frm.setPalette(pe)
        about_frm.show()

    def tab_changed(self, index):
        self.txt_pre_info.setPlainText('')
        self.show_review_doc.clear()
        if index == 0:
            if user_info.get_value('PART') == '质量部':
                self.save_unpass.setVisible(True)
                self.show_test_win.setVisible(True)
            else:
                self.save_unpass.setVisible(False)
                self.show_test_win.setVisible(False)
        elif index == 1:
            # set privileges
            if not user_info.get_value('PRIVILEGE'):
                self.btn_save_pre.setEnabled(False)
            try:
                self._load_tbl_pre_data()
            except Exception as e:
                user_info.log2txt(e)
            self.txt_pre_info.setEnabled(False)
            self.btn_save_pre.clicked.connect(self.save_pre_info)
        elif index == 2:
            self._load_on_follow_view_data()
            self.on_follow_view.clicked.connect(self.show_deal_method)
            self.follow_btn_search.clicked.connect(self.search_follow_item)

    def _load_on_follow_view_data(self):
        # fields will be ['ID', 'CaseClose', '批号', '不良品名称', '数量Kg', '处理次数', '不良剩余Kg', '客户']
        on_follow_sql = "SELECT A.ID,IF(A.case_closed_flag=TRUE,'Closed','Following'),A.批号,A.不良品名称,A.数量Kg,B.处理次数, " \
                        "If(ISNULL(B.dealed_q),A.数量Kg,A.数量Kg-B.dealed_q) AS 不良剩余Kg,A.客户 " \
                        "FROM (SELECT a.ID,客户,不良品名称,批号,数量Kg,case_closed_flag FROM 不合格品登记 " \
                        "AS a INNER JOIN 状态标记 AS b ON a.ID = b.ID WHERE " \
                        "review_finish=True) AS A LEFT JOIN (SELECT ID, SUM(处理数量Kg) AS " \
                        "dealed_q, COUNT(*) AS 处理次数 FROM Fcase_DealLog GROUP BY ID) AS B " \
                        "ON A.ID = B.ID;"
        self.set_on_follow_view_data(on_follow_sql)

    def _load_tbl_pre_data(self):
        current_part = user_info.get_value('PART')
        other_fields = ','.join(FIELDS_PRE[2:-2])
        # fields will be ['ID', '本部评审', '批号', '不良品名称', '客户', '生产日期', '数量Kg', '不良品种类', 'Review Finish', 'To_General']
        if current_part != '总经办' and current_part != '质量部':
            pre_info_sql = "SELECT a.ID,IF({2}评审=TRUE,'完成','未完成'),{0},IF(review_finish=TRUE,'YES','NO'),IF(g_m_rev=TRUE,'YES','NO') " \
                           "FROM 不合格品登记 a INNER JOIN 状态标记 b ON a.ID=b.ID " \
                           "WHERE b_m_rev=TRUE " \
                           "AND case_closed_flag=False " \
                           "AND FIND_IN_SET('{1}',part_need_review)" \
                           "".format(other_fields, current_part, current_part)
            self.set_tbl_pre(FIELDS_PRE, pre_info_sql)
        elif current_part == '质量部':
            pre_info_sql = "SELECT a.ID,IF({2}评审=TRUE,'完成','未完成'),{0},IF(review_finish=TRUE,'YES','NO'),IF(g_m_rev=TRUE,'YES','NO') " \
                           "FROM 不合格品登记 a INNER JOIN 状态标记 b ON a.ID=b.ID " \
                           "WHERE b_m_rev=TRUE " \
                           "AND case_closed_flag=False " \
                           "".format(other_fields, current_part, current_part)
            self.set_tbl_pre(FIELDS_PRE, pre_info_sql)
        elif current_part == '总经办':
            general_fields = ['ID', '本部评审', '批号', '不良品名称', '客户', '生产日期', '数量Kg', '不良品种类']
            pre_info_sql = "SELECT a.ID,IF({2}评审=TRUE,'YES','NO'),{0} " \
                           "FROM 不合格品登记 a INNER JOIN 状态标记 b ON a.ID=b.ID " \
                           "WHERE g_m_rev=TRUE " \
                           "AND case_closed_flag=False " \
                           "".format(other_fields, current_part, current_part)
            self.set_tbl_pre(general_fields, pre_info_sql)

    def save_pre_info(self):
        try:
            row = self.pre_tbl_view.currentIndex().row()
            unpass_id = int(self.model_pre.item(row, 0).text())
            part = user_info.get_value('PART')
            pre_information = self.txt_pre_info.toPlainText()
            if pre_information.replace(' ', ''):
                _db = MysqlDb()
                sql_pre_chk = "UPDATE 不合格品登记 SET {}评审=True WHERE ID={}" \
                              "".format(part, unpass_id)
                sql_pre_info = "UPDATE 状态标记 SET {}评审信息='{}' WHERE ID={}" \
                               "".format(part, pre_information, unpass_id)
                with _db:
                    try:
                        _db._cursor.execute(sql_pre_chk)
                        _db._cursor.execute(sql_pre_info)
                        eval('self.{}.setText(pre_information)'
                             ''.format(dict(zip(FIELDS_IN_TAB2.values(),
                                                FIELDS_IN_TAB2.keys()))[part+'评审信息']))
                        _db._cnn.commit()
                        QMessageBox.information(self, 'Information', '已保存！')
                        self._load_tbl_pre_data()
                    except Exception as e:
                        _db._cnn.rollback()
                        user_info.log2txt('提交写入评审信息时出现错误<save_pre_info>：<{}>'.format(e))
                        QMessageBox.critical(self, 'Mistake', '系统错误未保存！')
        except Exception as e:
            user_info.log2txt('试图保存评审信息时出现错误<save_pre_info>：<{}>'.format(e))
            pass

    def _pre_sign(self):
        old_cont = self.txt_pre_info.toPlainText()
        sign_info = "\t>>>{}\n\t>>>{}" \
                    "".format(user_info.get_value('USERNAME'),
                              datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.txt_pre_info.setPlainText(old_cont + '\n' + sign_info)

    def set_tbl_unpass(self, sql):
        """SET data for QTableView"""
        self.model_unpass = get_model(FIELDS_UNPASS, sql)
        self.tbl_unpass.setModel(self.model_unpass)
        self.set_tbl_format('tbl_unpass')

    def set_tbl_pre(self, fields, sql):
        self.model_pre = get_model(fields, sql)
        self.pre_tbl_view.setModel(self.model_pre)
        self.set_tbl_format('pre_tbl_view')

    def set_on_follow_view_data(self, sql):
        self.model_on_follow = get_model(FIELDS_FOLLOW_VIEW, sql)
        for i in range(self.model_on_follow.rowCount()):
            current_item = self.model_on_follow.item(i, 6)
            if float(current_item.text()) != 0:
                current_item.setForeground(QBrush(QColor(255, 0, 0)))
        self.on_follow_view.setModel(self.model_on_follow)
        self.set_tbl_format('on_follow_view')

    def set_tbl_format(self, tbl_name):
        tbl_view = self.findChild(QTableView, tbl_name)
        font = QFont("Consolas", 9)
        tbl_view.setFont(font)  # set font
        tbl_view.resizeColumnsToContents()  # set column width to fit contents (set font first!)
        tbl_view.setSortingEnabled(True)  # enable sorting
        tbl_view.verticalHeader().hide()  # hide vertical Header
        tbl_view.setEditTriggers(QTableView.NoEditTriggers)  # set table ReadOnly
        # self.tbl_unpass.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tbl_view.horizontalHeader().setStretchLastSection(True)  # last column stretch to full
        tbl_view.setSelectionBehavior(QTableView.SelectRows)  # set select entire row
        tbl_view.setSelectionMode(QTableView.SingleSelection)  # select only one

    def rclick_tbl_unpass(self):
        popMenu = QMenu()
        submenu_caseto = QMenu('CaseTo')
        submenu_caseto.setIcon(QIcon('icons/user.ico'))
        for part in user_info.get_value('PARTS')[:-1]:
            submenu_caseto.addAction(QAction(part, self))
        action_del = QAction('Delete', self)
        action_del.setIcon(QIcon('icons/delete_file_32px.ico'))
        action_part_preview = QAction('Start Department Review', self)
        action_part_preview.setIcon(QIcon('icons/parameterreview_32px.ico'))
        action_flush = QAction('刷新', self)
        action_flush.setIcon(QIcon('icons/dir.png'))
        action_typeidea = QAction('输入处理意见', self)
        action_typeidea.setIcon(QIcon('icons/input_tablet_32px.ico'))
        if user_info.get_value('PART') != '质量部':
            for ctl in [action_del, action_part_preview, submenu_caseto]:
                ctl.setEnabled(False)
        popMenu.addMenu(submenu_caseto)
        popMenu.addAction(action_del)
        popMenu.addAction(action_part_preview)
        popMenu.addAction(action_flush)
        popMenu.addAction(action_typeidea)
        popMenu.triggered.connect(self.processtrigger_tbl_unpass)
        popMenu.exec_(QCursor.pos())

    def processtrigger_tbl_unpass(self, act):
        row = self.tbl_unpass.currentIndex().row()
        if row != -1:
            unpass_id = int(self.model_unpass.item(row, 0).text())
            to_parts = user_info.get_value('PARTS')[:-1]
            sql = ''
            try:
                _db = MysqlDb()
                with _db:
                    if act.text() in to_parts:
                        sql = "UPDATE 状态标记 SET caseto_by_QA='{}' WHERE ID={}".format(act.text(), unpass_id)
                    elif act.text() == 'Delete':
                        sql = 'DELETE FROM 不合格品登记 WHERE ID = %d' % unpass_id
                        try:
                            _db.modify_db("DELETE FROM 状态标记 WHERE ID = %d" % unpass_id)
                        except Exception as e:
                            user_info.log2txt(e)
                    elif act.text() == 'Start Department Review':
                        sql = "UPDATE 状态标记 SET b_m_rev=True WHERE ID={}".format(unpass_id)
                    elif act.text() == '刷新':
                        self.set_tbl_unpass(TBL_UNPASS_SQL)
                    elif act.text() == '输入处理意见':
                        idea_dia = IdeaDialog(self, user_info.get_value('USERNAME'), user_info.get_value('PART'), unpass_id)
                        idea_dia.show()
                    _db.modify_db(sql)
                    self.fuzzy_search()
            except Exception as e:
                user_info.log2txt('右键操作不合格清单列表<ID={}>时出现错误<processtrigger_tbl_unpass>：<{}>'.format(unpass_id, e))
                pass

    def rclick_tbl_pre(self):
        popMenu = QMenu()
        action_to_gm = QAction('Start General Review')
        action_to_gm.setIcon(QIcon('icons/general_manager_128px.ico'))
        action_review_finish = QAction('Flag Review Finish')
        action_review_finish.setIcon(QIcon('icons/confirm128px.ico'))
        popMenu.addAction(action_to_gm)
        popMenu.addAction(action_review_finish)

        if user_info.get_value('PART') != '质量部':
            action_to_gm.setEnabled(False)
            action_review_finish.setEnabled(False)

        popMenu.triggered.connect(self.processtrigger_tbl_pre)
        popMenu.exec_(QCursor.pos())

    def processtrigger_tbl_pre(self, act):
        row = self.pre_tbl_view.currentIndex().row()
        sql = ''
        if row != -1:
            unpass_id = int(self.model_pre.item(row, 0).text())
            _db = MysqlDb()
            with _db:
                if act.text() == 'Start General Review':
                    sql = "UPDATE 状态标记 SET g_m_rev=True WHERE ID={}".format(unpass_id)
                elif act.text() == 'Flag Review Finish':
                    sql = "UPDATE 状态标记 SET review_finish=True WHERE ID={}".format(unpass_id)
                try:
                    _db.modify_db(sql)
                    self._load_tbl_pre_data()
                except Exception as e:
                    user_info.log2txt('第二页右键更新评审信息状态时发生错误：{}'.format(e))

    def rclick_follow_view(self):
        popMenu = QMenu()
        action_close_case = QAction('Close Case')
        action_close_case.setIcon(QIcon('icons/delete_file_32px.ico'))
        action_add_method = QAction('添加处置')
        action_add_method.setIcon(QIcon('icons/dealidea.ico'))
        action_flush = QAction('刷新')
        action_flush.setIcon(QIcon('icons/dir.png'))

        popMenu.addAction(action_close_case)
        popMenu.addAction(action_add_method)
        popMenu.addAction(action_flush)

        if user_info.get_value('PART') != '质量部':
            action_close_case.setEnabled(False)

        popMenu.triggered.connect(self.processtrigger_follow_view)
        popMenu.exec_(QCursor.pos())

    def processtrigger_follow_view(self, act):
        row = self.on_follow_view.currentIndex().row()
        if row != -1:
            unpass_id = int(self.model_on_follow.item(row, 0).text())
            _db = MysqlDb()
            with _db:
                if act.text() == 'Close Case':
                    sql = "UPDATE 状态标记 SET case_closed_flag=True WHERE ID={}".format(unpass_id)
                    try:
                        _db.modify_db(sql)
                        self._load_on_follow_view_data()
                        self.set_tbl_unpass(TBL_UNPASS_SQL)
                    except Exception as e:
                        user_info.log2txt('第三页右键更新跟踪信息状态时发生错误：{}'.format(e))
                elif act.text() == '添加处置':
                    count_rst = _db.get_rst("SELECT COUNT(*) as _count FROM fcase_deallog WHERE ID={}".format(unpass_id))
                    count = count_rst[0]['_count']
                    add_method_frm = AddMethod(self)
                    add_method_frm.line_unpass_id.setText(str(unpass_id))
                    add_method_frm.line_deal_id.setText('{}-{}'.format(str(unpass_id), str(count+1)))
                    add_method_frm.show()
                    add_method_frm.move(QCursor.pos())
                elif act.text() == '刷新':
                    self._load_on_follow_view_data()

    def fuzzy_search(self):
        keyword = self.lineEdit_11.text()
        search_str = " AND CONCAT(批号,不良品名称) LIKE '%{}%'".format(keyword) if keyword else ""
        fuzzy_sql = TBL_UNPASS_SQL + search_str
        self.set_tbl_unpass(fuzzy_sql)

    def search_follow_item(self):
        keyword = self.following_keyword.text()
        on_follow_sql = "SELECT A.ID,IF(A.case_closed_flag=TRUE,'Closed','Following'),A.批号,A.不良品名称,A.数量Kg,B.处理次数, " \
                        "If(ISNULL(B.dealed_q),A.数量Kg,A.数量Kg-B.dealed_q) AS 不良剩余Kg,A.客户 " \
                        "FROM (SELECT a.ID,客户,不良品名称,批号,数量Kg,case_closed_flag FROM 不合格品登记 " \
                        "AS a INNER JOIN 状态标记 AS b ON a.ID = b.ID WHERE " \
                        "review_finish=True) AS A LEFT JOIN (SELECT ID, SUM(处理数量Kg) AS " \
                        "dealed_q, COUNT(*) AS 处理次数 FROM Fcase_DealLog GROUP BY ID) AS B " \
                        "ON A.ID = B.ID WHERE CONCAT(A.批号,A.不良品名称) LIKE '%{}%'".format(keyword)
        self.set_on_follow_view_data(on_follow_sql)

    def show_select_parts_frm(self):
        frm = PartsNeeds(self)
        frm.move(QCursor.pos().x(),
                 QCursor.pos().y() - 350)  # form pos follow to the cursor
        frm.show()

    def show_unpass_item(self):
        row = self.tbl_unpass.currentIndex().row()
        unpass_id = int(
            self.model_unpass.item(row, 0).text())  # pos(row, 0) the first column
        try:
            _db = MysqlDb()
            with _db:
                fd = ','.join(list(FIELDS_IN_TAB1.values())[1:])
                sql = "SELECT a.ID,{0} FROM" \
                      " 不合格品登记 a LEFT JOIN 状态标记 b " \
                      "ON a.ID=b.ID " \
                      "WHERE a.ID={1}".format(fd, unpass_id)
                _rst = _db.get_rst(sql)
            values = list(_rst[0].values())
            fd = list(FIELDS_IN_TAB1.keys())
            for i in range(len(fd)):
                try:
                    v = values[i] if values[i] is not None else ''
                    exec_str = 'self.{}.setText(str(v))'.format(fd[i])
                    if fd[i] == 'pre_check':
                        exec_str = 'self.{}.setChecked(v)'.format(fd[i])
                    elif fd[i] == 'prodate':
                        exec_str = 'self.{}.setText(v.strftime("%Y-%m-%d"))'.format(fd[i])
                    eval(exec_str)
                except Exception as e:
                    user_info.log2txt('单击显示不合格项目<ID={}>时出现错误<show_unpass_item>：<{}>'.format(unpass_id, e))
                    pass
        except Exception as e:
            user_info.log2txt(e)

        if self.person.text() != '' and self.person.text() != user_info.get_value(
                'USERNAME'):
            self.btn_save.setEnabled(False)
            self.pre_check.setEnabled(False)
            self.btn_slparts.setEnabled(False)
        else:
            self.btn_save.setEnabled(True)
            self.pre_check.setEnabled(True)
            self.btn_slparts.setEnabled(True)

    def show_pre_item(self):
        self.txt_pre_info.setEnabled(True)
        row = self.pre_tbl_view.currentIndex().row()
        unpass_id = int(self.model_pre.item(row, 0).text())
        _db = MysqlDb()
        with _db:
            fd = ','.join(FIELDS_IN_TAB2.values())
            sql = "SELECT {} FROM 不合格品登记 a INNER JOIN 状态标记 b ON a.ID=b.ID WHERE a.ID={}" \
                  "".format(fd, unpass_id)
            pre_rst = _db.get_rst(sql)
        for obj_name in FIELDS_IN_TAB2.keys():
            try:
                eval("self.{}.setText(pre_rst[0]['{}'])"
                     "".format(obj_name, FIELDS_IN_TAB2[obj_name]))
            except Exception as e:
                print(e)
                pass

    def show_deal_method(self):
        """also show other information"""
        row = self.on_follow_view.currentIndex().row()
        unpass_id = int(self.model_on_follow.item(row, 0).text())
        # start show other information
        fields_handle_view = ['序号', '填写人', '处理数量Kg', '处理日期', '处理措施']
        sql = "SELECT deal_id,填写人,处理数量Kg,处理日期,处理措施 FROM fcase_deallog WHERE ID={}".format(unpass_id)
        model = get_model(fields_handle_view, sql)
        self.handle_view.setModel(model)
        self.set_tbl_format('handle_view')

        fields = ['不良品种类'] + list(FIELDS_IN_TAB3.values())[5:]
        self.show_review_doc.clear()
        _db = MysqlDb()
        with _db:
            fd = ','.join(fields)
            sql = "SELECT {} FROM 不合格品登记 a INNER JOIN 状态标记 b ON a.ID=b.ID WHERE a.ID={}" \
                  "".format(fd, unpass_id)
            pre_rst = _db.get_rst(sql)
        d = pre_rst[0]
        for k in fields:
            con = d[k]
            con = '' if con is None else con
            line = '<font size=5 color=blue>{}<font size=3 color=green> : {}</font></font>'.format(k, con)
            self.show_review_doc.append(line)

    def save(self):
        if self.ID.text():
            username = user_info.get_value('USERNAME')
            save_time = datetime.now().strftime('%Y-%m-%d %H:%M')
            _db = MysqlDb()
            with _db:
                sql = "UPDATE 不合格品登记 " \
                      "SET 原因分析='{0}',纠正措施='{1}',预防措施='{2}',自审人='{3}',自审时间='{4}',责任自审={5} " \
                      "WHERE ID={6}".format(self.result.toPlainText(),
                                            self.correctiveaciton.toPlainText(),
                                            self.precaution.toPlainText(), username,
                                            save_time, self.pre_check.isChecked(),
                                            int(self.ID.text()))
                _db.modify_db(sql)
            QMessageBox.information(self, 'Information', '已保存')
            self.person.setText(username)
            self.pre_time.setText(save_time)

    def preview(self):
        if self.pre_check.isChecked():
            s = QMessageBox.question(self, '提交处理单', '<自审人：{}>， <提交时间：{}>'.format(
                user_info.get_value('USERNAME'),
                datetime.now().strftime('%Y-%m-%d %H:%M')))
            if s == QMessageBox.Yes:
                contents = [ctl.toPlainText().replace(' ', '') for ctl in
                            (self.result, self.correctiveaciton, self.precaution)]
                contents.append(self.parts.text())
                if all(contents):
                    self.save()  # update db
                else:
                    QMessageBox.warning(self, '处理信息不全', '完成原因分析，纠正措施，预防措施及需参与的评审部门后提交！')
                    self.pre_check.setChecked(False)
            else:
                self.pre_check.setChecked(False)
        else:
            s = QMessageBox.question(self, '撤销提交', '<自审人：{}>， <提交时间：{}>'.format(
                user_info.get_value('USERNAME'),
                datetime.now().strftime('%Y-%m-%d %H:%M')))
            if s == QMessageBox.Yes:
                self.save()  # update db
            else:
                self.pre_check.setChecked(True)
