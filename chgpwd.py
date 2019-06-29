import user_info

from getdb import MysqlDb
from ui_chgpwd import Ui_chgpwd

from PyQt5.QtWidgets import QDialog, QMessageBox


class ChgPwd(QDialog, Ui_chgpwd):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.line_pwd_one.setFocus()
        self.buttonBox.accepted.connect(self.save_new_pwd)

    def save_new_pwd(self):
        pwd = self.line_pwd_one.text()
        pwd_again = self.line_pwd_again.text()
        if pwd == pwd_again and pwd:
            user_name = user_info.get_value('USERNAME')
            print(user_name)
            sql = 'UPDATE 用户 SET 密码="{}" WHERE 用户名="{}"'.format(pwd, user_name)
            try:
                db = MysqlDb()
                with db:
                    db.modify_db(sql)
                QMessageBox.information(self, '完成提示', '密码修改成功！')
            except Exception as e:
                user_info.log2txt('更改用户密码时错误：<{}>'.format(e))
        else:
            QMessageBox.warning(self, '错误提示', '输入有误！')
            self.show()  # keep use this dialog when need not quit
