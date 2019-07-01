import user_info
from ui_add_method import Ui_add_method
from getdb import MysqlDb

from datetime import datetime
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog


class AddMethod(QDialog, Ui_add_method):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.date_deal.setDate(QDate.currentDate())
        double_validator = QDoubleValidator()
        self.line_deal_qty.setValidator(double_validator)
        self.btn_save_method.clicked.connect(self.save_method)

    def save_method(self):
        deal_id = self.line_deal_id.text()
        id = self.line_unpass_id.text()
        method = self.txt_deal_method.toPlainText()
        deal_qty = self.line_deal_qty.text()
        deal_qty = float(deal_qty) if deal_qty else 0
        deal_date = self.date_deal.text()
        person = user_info.get_value('USERNAME')
        wr_time = datetime.now().__format__("%Y-%m-%d %H:%M")
        if deal_date and deal_qty and method:
            sql = "INSERT INTO fcase_deallog VALUES('{}',{},'{}','{}','{}','{}','{}')" \
                  "".format(deal_id, id, method, deal_qty, deal_date, person, wr_time)
            db = MysqlDb()
            with db:
                try:
                    db.modify_db(sql)
                    self.parent.show_deal_method()
                    self.close()
                except Exception as e:
                    user_info.log2txt('添加新的处理（id=<{}>)记录时<error>: {}'.format(id, e))

