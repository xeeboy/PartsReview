import user_info
import mainwindow

from ui_new_unpass import *
from getdb import MysqlDb

from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QDoubleValidator


class NewUnpass(QDialog, Ui_new_unpass):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        db = MysqlDb()
        with db:
            self.rst = db.get_rst("SELECT DISTINCT 客户,产品型号 FROM 产品信息")
            count_rst = db.get_rst("SELECT MAX(ID) AS above_id FROM 不合格品登记")
            count = count_rst[0]['above_id']
        self.new_id.setText(str(count + 1))
        self.comb_new_coustom.addItems(set(r['客户'] for r in self.rst))
        self.comb_new_coustom.setCurrentIndex(-1)
        self.comb_new_coustom.currentTextChanged.connect(self.set_unpassname_items)
        self.new_unpasstype.addItems(('制程不合格', '退货不合格', '来料不合格'))
        self.parent = parent
        self.date_produce.setDate(QDate.currentDate())
        self.new_unpass_qty.setValidator(QDoubleValidator())
        self.btn_clear.clicked.connect(self.clear_unpass_info)
        self.btn_save_new_unpass.clicked.connect(self.save_new_unpass)

    def set_unpassname_items(self, coustomer):
        self.comb_new_unpassname.clear()  # remove all current items
        self.comb_new_unpassname.addItems((r['产品型号'] for r in self.rst if r['客户'] == coustomer))

    def clear_unpass_info(self):
        for ctl in [self.new_batch, self.new_unpass_qty, self.new_unpass_desc]:
            ctl.clear()
        self.comb_new_coustom.setCurrentIndex(-1)
        self.comb_new_unpassname.setCurrentIndex(-1)
        self.date_produce.setDate(QDate.currentDate())

    def save_new_unpass(self):
        batch, prodate, unpasstype, unpassname, unpassqty, describe, customer, new_id = \
            self.new_batch.text(), self.date_produce.text(), self.new_unpasstype.currentText(), \
            self.comb_new_unpassname.currentText(), self.new_unpass_qty.text(), self.new_unpass_desc.toPlainText(), \
            self.comb_new_coustom.currentText(), self.new_id.text()
        if all([batch, prodate, unpasstype, unpassname, unpassqty, describe, customer]):
            sql = "INSERT INTO 不合格品登记 (批号,生产日期,不良品种类,不良品名称,数量Kg,不合格描述,客户,ID) " \
                  "VALUES ('{}','{}','{}','{}','{}','{}','{}',{})" \
                  "".format(batch, prodate, unpasstype, unpassname, unpassqty,
                            describe, customer, new_id)
            _db = MysqlDb()
            with _db:
                try:
                    _db.modify_db(sql)
                    _db.modify_db("INSERT INTO 状态标记 SET ID={}".format(new_id))
                    self.new_id.setText(str(int(self.new_id.text()) + 1))
                    self.parent.set_tbl_unpass(mainwindow.TBL_UNPASS_SQL)
                    QMessageBox.information(self, '操作提示', '插入成功')
                    self.clear_unpass_info()
                except Exception as e:
                    user_info.log2txt('登记新不合格品时发生错误：{}'.format(e))
        else:
            QMessageBox.warning(self, '警告', '缺少必要信息,请完善后保存！')
