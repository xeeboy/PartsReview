import user_info

from ui_main import *
from getdb import *
from ui_part_need_review import *
from sysrun import *
from PyQt5.QtWidgets import QMainWindow, QTableView, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QFont

FIELDS_UNPASS = ['ID', '客户', '批号', '不良品名称', '责任部门', '技术部意见', '工艺部意见', '质量部意见', '技术支持部意见', '总经办意见']
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
                  'pre_check': '责任自审'
                  }

idea = ','.join(("IIF(ISNULL({}) or {}='','待输入','已更新')".format(part_idea, part_idea) for part_idea in
                 ('技术部意见', '工艺部意见', '质量部意见', '技术支持部意见', '总经办意见')))

TBL_UNPASS_SQL = "SELECT a.ID,客户,批号,不良品名称,caseto_by_QA as 责任部门,{}" \
                 " FROM 不合格品登记 a LEFT JOIN 状态标记 b ON a.ID=b.ID".format(idea)

CURRENT_USERNAME = user_info.get_value('USERNAME')
CURRENT_PART = user_info.get_value('PART')


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_tbl_unpass(TBL_UNPASS_SQL)
        self.btn_search.clicked.connect(self.fuzzy_search)
        self.lineEdit_11.setPlaceholderText('批号或者不良品名称关键字')
        self.btn_slparts.clicked.connect(self.show_select_parts_frm)
        self.tbl_unpass.clicked.connect(self.show_unpass_item_info)

    def set_tbl_unpass(self, sql):
        self.model = get_model(FIELDS_UNPASS, sql)
        self.tbl_unpass.setModel(self.model)
        font = QFont("Arial", 9)
        self.tbl_unpass.setFont(font)   # set font
        self.tbl_unpass.resizeColumnsToContents()  # set column width to fit contents (set font first!)
        self.tbl_unpass.setSortingEnabled(True)  # enable sorting
        self.tbl_unpass.verticalHeader().hide()
        self.tbl_unpass.setEditTriggers(QTableView.NoEditTriggers)   # set table ReadOnly
        self.tbl_unpass.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # set full show table
        self.tbl_unpass.setSelectionBehavior(QTableView.SelectRows)  # set select entire row
        self.tbl_unpass.setSelectionMode(QTableView.SingleSelection)  # select only one

    def fuzzy_search(self):
        keyword = self.lineEdit_11.text()
        SearchStr = " WHERE a.批号 & a.不良品名称 LIKE '%{}%'".format(keyword) if keyword else ""
        fuzzy_sql = TBL_UNPASS_SQL + SearchStr
        self.set_tbl_unpass(fuzzy_sql)

    def show_select_parts_frm(self):
        frm = PartsNeeds(self)
        frm.move(100, 500)
        frm.show()

    def show_unpass_item_info(self):
        row = self.tbl_unpass.currentIndex().row()
        unpass_id = int(self.model.item(row, 0).text())
        db = AccDb()
        with db:
            fd = ','.join(FIELDS_IN_TAB1.values())
            sql = "select {0} from 不合格品登记 where ID={1}".format(fd, unpass_id)
            rst = db.get_rst(sql)
        values = rst[0]
        fd = list(FIELDS_IN_TAB1.keys())
        for i in range(len(fd)):
            try:
                v= values[i] if values[i] is not None else ''
                exec_str = 'self.{}.setText(str(v))'.format(fd[i])
                if fd[i] == 'ID':
                    exec_str = 'self.{}.setText("%06d" % v)'.format(fd[i])
                elif fd[i] == 'pre_check':
                    exec_str = 'self.{}.setChecked(v)'.format(fd[i])
                elif fd[i] == 'prodate':
                    exec_str = 'self.{}.setText(v.strftime("%Y-%m-%d"))'.format(fd[i])
                eval(exec_str)
            except:
                pass

        print(CURRENT_PART, CURRENT_USERNAME)