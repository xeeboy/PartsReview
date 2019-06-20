from ui_main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from getdb import AccDb
FIELDS_UNPASS = ['ID', '客户', '批号', '不良品种类', '不良品名称', '责任部门']



class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_tbl_unpass()

    def set_tbl_unpass(self):
        """init tableview 'tbl_unpass'"""
        db = AccDb()
        model = QStandardItemModel()
        with db:
            sql = "SELECT a.ID,客户,批号,不良品种类,不良品名称,caseto_by_QA as 责任部门 FROM 不合格品登记 a LEFT JOIN 状态标记 b ON a.ID=b.ID ORDER BY a.ID DESC"
            rst = db.get_rst(sql)
        n = len(rst)
        for i in range(len(FIELDS_UNPASS)):
            item = QStandardItem(FIELDS_UNPASS[i])
            model.setHorizontalHeaderItem(i, item)
        for rown in range(n):
            for coln in range(len(FIELDS_UNPASS)):
                content = rst[rown][coln]
                if coln == 0:
                    content = '%06d' % content
                item = QStandardItem(content)
                # 在模型的指定位置添加数据(item)
                model.setItem(rown, coln, item)

        self.tbl_unpass.setModel(model)
        font = QFont("Arial", 11)
        self.tbl_unpass.setFont(font)   # set font
        self.tbl_unpass.resizeColumnsToContents()  # set column width to fit contents (set font first!)
        self.tbl_unpass.setSortingEnabled(True)  # enable sorting
        self.tbl_unpass.verticalHeader().hide()
        self.tbl_unpass.setEditTriggers(QAbstractItemView.NoEditTriggers)   # set table readonly
        self.tbl_unpass.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # set full show table
        self.tbl_unpass.setSelectionBehavior(QAbstractItemView.SelectRows)  # set select entire row