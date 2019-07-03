import user_info

from ui_qa_data import *
from getdb import MysqlDb, get_model

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel


class AddDataForm(QtWidgets.QMainWindow, Ui_QAData):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.date_produce.setDate(QDate.currentDate())
        self.date_test.setDate(QDate.currentDate())
        self.btn_test_clear.clicked.connect(self.clear_pro_info)
        db = MysqlDb()
        with db:
            self.rst = db.get_rst("SELECT DISTINCT 客户,产品型号,颜色 FROM 产品信息")
        self.comb_test_coustomer.addItems(set(r['客户'] for r in self.rst))
        self.comb_test_coustomer.setCurrentIndex(-1)
        self.comb_test_coustomer.currentTextChanged.connect(self.set_pro_type_items)
        self.comb_pro_type.currentTextChanged.connect(self.set_pro_color_items)
        self.btn_test_save.clicked.connect(self.save_pro_info)
        self.set_test_data_view()

    def set_pro_type_items(self, coustomer):
        self.comb_pro_type.clear()  # remove all current items
        self.comb_pro_type.addItems(
            set((r['产品型号'] for r in self.rst if r['客户'] == coustomer)))

    def set_pro_color_items(self, pro_name):
        self.comb_pro_color.clear()
        self.comb_pro_color.addItems(
            set((r['颜色'] for r in self.rst if r['产品型号'] == pro_name)))

    def clear_pro_info(self):
        self.test_batch.setText(None)
        self.comb_test_coustomer.setCurrentIndex(-1)
        self.comb_pro_type.setCurrentIndex(-1)
        self.comb_pro_color.setCurrentIndex(-1)
        self.date_produce.setDate(QDate.currentDate())
        self.date_test.setDate(QDate.currentDate())

    def save_pro_info(self):
        batch, coustomer, pro_name, pro_color, pro_date, test_date = \
            self.test_batch.text(), self.comb_test_coustomer.currentText(),\
            self.comb_pro_type.currentText(), self.comb_pro_color.currentText(), \
            self.date_produce.text(), self.date_test.text()
        if all([batch, coustomer, pro_name, pro_color, pro_date, test_date]):
            db = MysqlDb()
            with db:
                try:
                    sql_info = "INSERT INTO 产品信息 (批号, 客户, 产品型号, 颜色, 生产日期, 检验日期)" \
                          " VALUES ('{}', '{}', '{}', '{}', '{}', '{}')" \
                          "".format(batch, coustomer, pro_name, pro_color, pro_date, test_date)
                    sql_performance = "INSERT INTO 常规性能 SET 批号='{}'".format(batch)
                    db._cursor.execute(sql_info)
                    db._cursor.execute(sql_performance)
                    db._cnn.commit()
                    QMessageBox.information(self, '操作提示', '插入成功')
                except Exception as e:
                    db._cnn.rollback()
                    QMessageBox.critical(self, '逻辑错误', '可能已存在相同的批号！')
                    user_info.log2txt('登记新产品信息时错误：{}'.format(e))
        else:
            QMessageBox.warning(self, '警告', '缺少必要产品信息！')

    def set_test_data_view(self):
        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName("localhost")
        db.setUserName("root")
        db.setPassword("123456")
        db.setPort(3306)
        db.setDatabaseName("qadb")
        ok = db.open()
        if not ok:
            print(db.lastError().text())
        else:
            print('connect')


