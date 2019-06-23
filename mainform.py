import user_info

from ui_main import *
from getdb import *
from ui_part_need_review import *
from sysrun import *

from datetime import datetime
from parts_idea import IdeaDialog
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableView, QHeaderView, QMenu, QAction
from PyQt5.QtGui import QStandardItemModel, QFont, QCursor, QIcon

FIELDS_UNPASS = ['ID', '客户', '批号', '不良品名称', '责任部门', '送部门评审', '送总经理评审', '技术部意见', '工艺部意见', '质量部意见', '技术支持部意见', '总经办意见']
FIELDS_IN_TAB1 = {'ID': 'ID',
                  'batch': '批号',
                  'prodate': '生产日期',
                  'unpasstype': '不良品种类',
                  'unpassname': '不良品名称',
                  'unpassqty': '数量Kg',
                  'describe': '不合格描述',
                  'result': '原因分析',
                  'correctiveaciton': '纠正措施',
                  'precaution': '预防措施',
                  'person': '自审人',
                  'pre_time': '自审时间',
                  'pre_check': '责任自审',
                  'parts': 'part_need_review'
                  }

idea = ','.join(("IIF(ISNULL({}) or {}='','待输入','已更新')".format(part_idea, part_idea) for part_idea in
                 ('技术部意见', '工艺部意见', '质量部意见', '技术支持部意见', '总经办意见')))

TBL_UNPASS_SQL = "SELECT a.ID,客户,批号,不良品名称,caseto_by_QA,IIF(b.b_m_rev=TRUE,'YES','NO')," \
                 "IIF(b.g_m_rev=TRUE,'YES','NO'),{} FROM 不合格品登记 a LEFT JOIN 状态标记 b ON a.ID=b.ID".format(idea)


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_tbl_unpass(TBL_UNPASS_SQL)
        self.btn_search.clicked.connect(self.fuzzy_search)
        self.lineEdit_11.setPlaceholderText('批号或者不良品名称关键字')
        self.btn_slparts.clicked.connect(self.show_select_parts_frm)
        self.tbl_unpass.clicked.connect(self.show_unpass_item_info)
        self.btn_save.clicked.connect(self.save)
        self.pre_check.clicked.connect(self.preview)
        self.tbl_unpass.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tbl_unpass.customContextMenuRequested.connect(self.rclick)

    def set_tbl_unpass(self, sql):
        self.model = get_model(FIELDS_UNPASS[:-1] + ['总经理意见'], sql)
        self.tbl_unpass.setModel(self.model)
        font = QFont("SimHei", 11)
        self.tbl_unpass.setFont(font)  # set font
        self.tbl_unpass.resizeColumnsToContents()  # set column width to fit contents (set font first!)
        self.tbl_unpass.setSortingEnabled(True)  # enable sorting
        self.tbl_unpass.verticalHeader().hide()
        self.tbl_unpass.setEditTriggers(QTableView.NoEditTriggers)  # set table ReadOnly
        # self.tbl_unpass.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Width of equalization column
        self.tbl_unpass.horizontalHeader().setStretchLastSection(True)  # last column stretch to full
        self.tbl_unpass.setSelectionBehavior(QTableView.SelectRows)  # set select entire row
        self.tbl_unpass.setSelectionMode(QTableView.SingleSelection)  # select only one

    def rclick(self):
        popMenu = QMenu()

        submenu_caseto = QMenu('CaseTo')
        submenu_caseto.setIcon(QIcon('icons/user.ico'))
        for part in user_info.get_value('PARTS')[:-1]:
            submenu_caseto.addAction(QAction(part, self))

        action_del = QAction('Delete', self)
        action_del.setIcon(QIcon('icons/delete_file_32px.ico'))
        action_part_preview = QAction('Start Department Preview', self)
        action_part_preview.setIcon(QIcon('icons/parameterreview_32px.ico'))
        action_general_preview = QAction('Start General Preview', self)
        action_general_preview.setIcon(QIcon('icons/general_manager_128px.ico'))
        action_typeidea = QAction('输入处理意见', self)
        action_typeidea.setIcon(QIcon('icons/input_tablet_32px.ico'))

        if user_info.get_value('PART') != '质量部':
            for ctl in [action_del, action_part_preview, action_general_preview, submenu_caseto]:
                ctl.setEnabled(False)

        popMenu.addMenu(submenu_caseto)
        popMenu.addAction(action_del)
        popMenu.addAction(action_part_preview)
        popMenu.addAction(action_general_preview)
        popMenu.addAction(action_typeidea)
        popMenu.triggered.connect(self.processtrigger)
        popMenu.exec_(QCursor.pos())

    def processtrigger(self, act):
        row = self.tbl_unpass.currentIndex().row()
        unpass_id = int(self.model.item(row, 0).text())
        to_parts = user_info.get_value('PARTS')[:-1]
        sql = ''
        try:
            db = AccDb()
            with db:
                if act.text() in to_parts:
                    sql = "update 状态标记 set caseto_by_QA='{}' where ID={}".format(act.text(), unpass_id)
                    if len(db.get_rst('select caseto_by_QA from 状态标记 where ID=%d' % unpass_id)) == 0:
                        sql = "insert into 状态标记(ID, caseto_by_QA) values({},'{}')".format(unpass_id, act.text())
                elif act.text() == 'Delete':
                    sql = 'delete * from 不合格品登记 where ID = %d' % unpass_id
                elif act.text() == 'Start Department Preview':
                    sql = "update 状态标记 set b_m_rev=True where ID={}".format(unpass_id)
                elif act.text() == 'Start General Preview':
                    sql = "update 状态标记 set g_m_rev=True where ID={}".format(unpass_id)
                elif act.text() == '输入处理意见':
                    # TODO show type in idea window
                    idea_dia = IdeaDialog(self, user_info.get_value('USERNAME'), user_info.get_value('PART'), unpass_id)
                    idea_dia.show()
                db.modify_db(sql)
            self.set_tbl_unpass(TBL_UNPASS_SQL)
        except:
            pass

    def fuzzy_search(self):
        keyword = self.lineEdit_11.text()
        search_str = " WHERE a.批号 & a.不良品名称 LIKE '%{}%'".format(keyword) if keyword else ""
        fuzzy_sql = TBL_UNPASS_SQL + search_str
        self.set_tbl_unpass(fuzzy_sql)

    def show_select_parts_frm(self):
        frm = PartsNeeds(self)
        frm.move(QCursor.pos().x(), QCursor.pos().y() - 350)  # form pos follow to the cursor
        frm.show()

    def show_unpass_item_info(self):
        row = self.tbl_unpass.currentIndex().row()
        unpass_id = int(self.model.item(row, 0).text())  # pos(row, 0) the first column
        db = AccDb()
        with db:
            fd = ','.join(list(FIELDS_IN_TAB1.values())[1:])
            sql = "select a.ID,{0} from 不合格品登记 a left join 状态标记 b on a.ID=b.ID where a.ID={1}".format(fd, unpass_id)
            _rst = db.get_rst(sql)
        values = _rst[0]
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
            except:
                pass

        if self.person.text() != '' and self.person.text() != user_info.get_value('USERNAME'):
            self.btn_save.setEnabled(False)
            self.pre_check.setEnabled(False)
            self.btn_slparts.setEnabled(False)
        else:
            self.btn_save.setEnabled(True)
            self.pre_check.setEnabled(True)
            self.btn_slparts.setEnabled(True)

    def save(self):
        if self.ID.text():
            username = user_info.get_value('USERNAME')
            savetime = datetime.now().strftime('%Y-%m-%d %H:%M')
            db = AccDb()
            with db:
                sql = "update 不合格品登记 set 原因分析='{0}',纠正措施='{1}',预防措施='{2}',自审人='{3}',自审时间='{4}',责任自审={5} where ID={6}".format(
                    self.result.toPlainText(), self.correctiveaciton.toPlainText(), self.precaution.toPlainText(),
                    username, savetime, self.pre_check.isChecked(), int(self.ID.text()))
                db.modify_db(sql)
            QMessageBox.information(self, 'Information', '已保存', )
            self.person.setText(username)
            self.pre_time.setText(savetime)

    def preview(self):
        if self.pre_check.isChecked():
            s = QMessageBox.question(self, '提交处理单', '<自审人：{}>， <提交时间：{}>'.format(user_info.get_value('USERNAME'),
                                                                                 datetime.now().strftime(
                                                                                     '%Y-%m-%d %H:%M')))
            if s == QMessageBox.Yes:
                contents = [ctl.toPlainText().replace(' ', '') for ctl in (
                    self.result, self.correctiveaciton, self.precaution)]
                contents.append(self.parts.text())
                if all(contents):
                    self.save()  # update db
                else:
                    QMessageBox.warning(self, '处理信息不全', '完成原因分析，纠正措施，预防措施及需参与的评审部门后提交！')
                    self.pre_check.setChecked(False)
            else:
                self.pre_check.setChecked(False)
        else:
            s = QMessageBox.question(self, '撤销提交', '<自审人：{}>， <提交时间：{}>'.format(user_info.get_value('USERNAME'),
                                                                                datetime.now().strftime(
                                                                                    '%Y-%m-%d %H:%M')))
            if s == QMessageBox.Yes:
                self.save()  # update db
            else:
                self.pre_check.setChecked(True)
