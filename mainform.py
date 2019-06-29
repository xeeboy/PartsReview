import user_info
from getdb import *
from ui_main import *
from ui_part_need_review import *
from parts_idea import IdeaDialog

from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableView, QMenu, QAction, QMessageBox
from PyQt5.QtGui import QFont, QCursor, QIcon

FIELDS_UNPASS = ['ID', '客户', '批号', '不良品名称', '责任部门', '送部门评审', '技术部意见', '工艺部意见',
                 '质量部意见', '技术支持部意见']
idea = ','.join(("IF(ISNULL({}) or {}='','待输入','已更新')"
                 "".format(part_idea, part_idea) for part_idea in FIELDS_UNPASS[-4:]))
TBL_UNPASS_SQL = "SELECT a.ID,客户,批号,不良品名称,caseto_by_QA,IF(b.b_m_rev=TRUE,'YES','NO'),{} " \
                 "FROM 不合格品登记 a LEFT JOIN 状态标记 b ON a.ID=b.ID".format(idea)
FIELDS_IN_TAB1 = {'ID': 'ID', 'batch': '批号', 'prodate': '生产日期', 'unpasstype': '不良品种类',
                  'unpassname': '不良品名称', 'unpassqty': '数量Kg', 'describe': '不合格描述',
                  'result': '原因分析', 'correctiveaciton': '纠正措施', 'precaution': '预防措施',
                  'person': '自审人', 'pre_time': '自审时间', 'pre_check': '责任自审',
                  'parts': 'part_need_review'}

FIELDS_PRE = ['ID', '评审状态', '批号', '不良品名称', '客户', '生产日期', '数量Kg', '不良品种类']
FIELDS_IN_TAB2 = {'pre_describle': '不合格描述', 'pre_result': '原因分析',
                  'pre_correctiveation': '纠正措施', 'pre_precaution': '预防措施',
                  'pre_tec_idea': '技术部意见', 'pre_pro_idea': '工艺部意见',
                  'pre_qa_idea': '质量部意见', 'pre_tec_support_idea': '技术支持部意见'}


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)

        # set tab1
        self.set_tbl_unpass(TBL_UNPASS_SQL)
        self.btn_slparts.clicked.connect(self.show_select_parts_frm)
        self.btn_save.clicked.connect(self.save)
        self.tbl_unpass.clicked.connect(self.show_unpass_item)
        self.pre_check.clicked.connect(self.preview)
        self.tbl_unpass.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tbl_unpass.customContextMenuRequested.connect(self.rclick_tbl_unpass)

        # TODO tab2 logic
        # set tab2
        self.pre_tbl_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pre_tbl_view.customContextMenuRequested.connect(self.rclick_tbl_pre)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.pre_tbl_view.clicked.connect(self.show_pre_item)  # self.pre_tbl_view.setMouseTracking(True)

    def tab_changed(self, index):
        if index == 1:
            # set privileges
            if not user_info.get_value('PRIVILEGE'):
                self.btn_save_pre.setEnabled(False)
            self._load_tbl_pre_data()
            self.txt_pre_info.setEnabled(False)
            self.btn_save_pre.clicked.connect(self.save_pre_info)
            self.btn_sign_pre.clicked.connect(self.pre_sign)

    def _load_tbl_pre_data(self):
        current_part = user_info.get_value('PART')
        other_fields = ','.join(FIELDS_PRE[2:])
        _m_flag = 'g_m_rev=True' if current_part == '总经办' else 'b_m_rev=True'
        pre_info_sql = "SELECT a.ID,IF({2}评审=TRUE,'YES','NO'),{0} " \
                       "FROM 不合格品登记 a INNER JOIN 状态标记 b ON a.ID=b.ID " \
                       "WHERE {3} " \
                       "AND case_closed_flag=False " \
                       "AND FIND_IN_SET('{1}',part_need_review)" \
                       "".format(other_fields, current_part, current_part, _m_flag)
        self.set_tbl_pre(pre_info_sql)

    # TODO save preview information
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
                        _db._cnn.commit()
                        QMessageBox.information(self, 'Information', '已保存！')
                        self._load_tbl_pre_data()
                    except Exception as e:
                        _db._cnn.rollback()
                        # TODO logging
                        print(e)
                        QMessageBox.critical(self, 'Mistake', '系统错误未保存！')
        except Exception as e:
            # TODO logging
            print(e)
            pass

    def pre_sign(self):
        old_cont = self.txt_pre_info.toPlainText()
        sign_info = "\t\t\t>>>评审人:{}\n\t\t\t>>>评审日期：{}" \
                    "".format(user_info.get_value('USERNAME'),
                              datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.txt_pre_info.setPlainText(old_cont + '\n' + sign_info)

    def set_tbl_unpass(self, sql):
        """SET data for QTableView"""
        self.model_unpass = get_model(FIELDS_UNPASS, sql)
        self.tbl_unpass.setModel(self.model_unpass)
        self.set_tbl_format('tbl_unpass')

    def set_tbl_pre(self, sql):
        self.model_pre = get_model(FIELDS_PRE, sql)
        self.pre_tbl_view.setModel(self.model_pre)
        self.set_tbl_format('pre_tbl_view')

    def set_tbl_format(self, tbl_name):
        _tbl_view = self.findChild(QTableView, tbl_name)
        font = QFont("SimHei", 10)
        _tbl_view.setFont(font)  # set font
        _tbl_view.resizeColumnsToContents()  # set column width to fit contents (set font first!)
        _tbl_view.setSortingEnabled(True)  # enable sorting
        _tbl_view.verticalHeader().hide()  # hide vertical Header
        _tbl_view.setEditTriggers(QTableView.NoEditTriggers)  # set table ReadOnly
        # self.tbl_unpass.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        _tbl_view.horizontalHeader().setStretchLastSection(
            True)  # last column stretch to full
        _tbl_view.setSelectionBehavior(QTableView.SelectRows)  # set select entire row
        _tbl_view.setSelectionMode(QTableView.SingleSelection)  # select only one

    def rclick_tbl_unpass(self):
        popMenu = QMenu()
        submenu_caseto = QMenu('CaseTo')
        submenu_caseto.setIcon(QIcon('icons/user.ico'))
        for part in user_info.get_value('PARTS')[:-1]:
            submenu_caseto.addAction(QAction(part, self))
        action_del = QAction('Delete', self)
        action_del.setIcon(QIcon('icons/delete_file_32px.ico'))
        action_part_preview = QAction('Start Department Preview', self)
        action_part_preview.setIcon(QIcon('icons/parameterreview_32px.ico'))
        action_typeidea = QAction('输入处理意见', self)
        action_typeidea.setIcon(QIcon('icons/input_tablet_32px.ico'))
        if user_info.get_value('PART') != '质量部':
            for ctl in [action_del, action_part_preview, submenu_caseto]:
                ctl.setEnabled(False)
        popMenu.addMenu(submenu_caseto)
        popMenu.addAction(action_del)
        popMenu.addAction(action_part_preview)
        popMenu.addAction(action_typeidea)
        popMenu.triggered.connect(self.processtrigger_tbl_unpass)
        popMenu.exec_(QCursor.pos())

    def processtrigger_tbl_unpass(self, act):
        row = self.tbl_unpass.currentIndex().row()
        unpass_id = int(self.model_unpass.item(row, 0).text())
        to_parts = user_info.get_value('PARTS')[:-1]
        sql = ''
        try:
            db = MysqlDb()
            with db:
                if act.text() in to_parts:
                    sql = "UPDATE 状态标记 SET caseto_by_QA='{}' WHERE ID={}".format(act.text(), unpass_id)
                    if len(db.get_rst('SELECT caseto_by_QA FROM 状态标记 WHERE ID=%d' % unpass_id)) == 0:
                        sql = "INSERT INTO 状态标记(ID, caseto_by_QA) VALUES({},'{}')".format(unpass_id, act.text())
                elif act.text() == 'Delete':
                    sql = 'DELETE FROM 不合格品登记 WHERE ID = %d' % unpass_id
                elif act.text() == 'Start Department Preview':
                    sql = "UPDATE 状态标记 SET b_m_rev=True WHERE ID={}".format(unpass_id)
                elif act.text() == '输入处理意见':
                    idea_dia = IdeaDialog(self, user_info.get_value('USERNAME'), user_info.get_value('PART'), unpass_id)
                    idea_dia.show()
                db.modify_db(sql)
                self.fuzzy_search()
        except Exception as e:
            # TODO logging
            print(e)
            pass

    def rclick_tbl_pre(self):
        popMenu = QMenu()
        action_to_gm = QAction('Start General Review')
        action_to_gm.setIcon(QIcon('icons/general_manager_128px.ico'))
        popMenu.addAction(action_to_gm)
        if user_info.get_value('PART') != '质量部':
            action_to_gm.setEnabled(False)
        popMenu.triggered.connect(self.processtrigger_tbl_pre)
        popMenu.exec_(QCursor.pos())

    def processtrigger_tbl_pre(self, act):
        row = self.pre_tbl_view.currentIndex().row()
        unpass_id = int(self.model_pre.item(row, 0).text())
        if act.text() == 'Start General Review':
            sql = "UPDATE 状态标记 SET g_m_rev=True WHERE ID={}".format(unpass_id)
            _db = MysqlDb()
            with _db:
                _db.modify_db(sql)
                QMessageBox.information(self, 'Information', '已送审')

    def fuzzy_search(self):
        keyword = self.lineEdit_11.text()
        search_str = " WHERE CONCAT(批号,不良品名称) LIKE '%{}%'".format(
            keyword) if keyword else ""
        fuzzy_sql = TBL_UNPASS_SQL + search_str
        self.set_tbl_unpass(fuzzy_sql)

    def show_select_parts_frm(self):
        frm = PartsNeeds(self)
        frm.move(QCursor.pos().x(),
                 QCursor.pos().y() - 350)  # form pos follow to the cursor
        frm.show()

    def show_unpass_item(self):
        row = self.tbl_unpass.currentIndex().row()
        unpass_id = int(
            self.model_unpass.item(row, 0).text())  # pos(row, 0) the first column
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
                # TODO logging
                pass

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
            sql = "SELECT {} FROM 不合格品登记 WHERE ID={}".format(fd, unpass_id)
            pre_rst = _db.get_rst(sql)
        for obj_name in FIELDS_IN_TAB2.keys():
            eval("self.{}.setText(pre_rst[0]['{}'])"
                 "".format(obj_name, FIELDS_IN_TAB2[obj_name]))

    def save(self):
        if self.ID.text():
            username = user_info.get_value('USERNAME')
            save_time = datetime.now().strftime('%Y-%m-%d %H:%M')
            db = MysqlDb()
            with db:
                sql = "UPDATE 不合格品登记 " \
                      "SET 原因分析='{0}',纠正措施='{1}',预防措施='{2}',自审人='{3}',自审时间='{4}',责任自审={5} " \
                      "WHERE ID={6}".format(self.result.toPlainText(),
                                            self.correctiveaciton.toPlainText(),
                                            self.precaution.toPlainText(), username,
                                            save_time, self.pre_check.isChecked(),
                                            int(self.ID.text()))
                db.modify_db(sql)
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
