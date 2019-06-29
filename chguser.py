import user_info

from getdb import MysqlDb
from ui_chguser import Ui_chguser

from PyQt5.QtWidgets import QDialog, QMessageBox


class ChgUser(QDialog, Ui_chguser):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.line_chg_user.setFocus()
        self.buttonBox.accepted.connect(self.change_info)

    def change_info(self):
        user = self.line_chg_user.text()
        pwd_again = self.line_chg_pwd.text()
        if user:
            db = MysqlDb()
            with db:
                sql = "SELECT 密码 FROM 用户 WHERE 用户名='{}'".format(user)
                try:
                    _rst = db.get_rst(sql)
                    if _rst:
                        check_pwd = _rst[0]['密码']
                        if pwd_again == check_pwd:
                            sql = "select 部门,邮箱,评审权限 from 用户 where 用户名='%s'" % user
                            user_info_rst = db.get_rst(sql)
                            _PARTS = db.get_rst('select 部门 from 部门')
                            PART = user_info_rst[0]['部门']
                            EMAIL = user_info_rst[0]['邮箱']
                            PRIVILEGE = user_info_rst[0]['评审权限']
                            user_info._init()
                            user_info.set_value('USERNAME', user)
                            user_info.set_value('PART', PART)
                            user_info.set_value('EMAIL', EMAIL)
                            user_info.set_value('PRIVILEGE', PRIVILEGE)
                            user_info.set_value('PARTS', [p['部门'] for p in _PARTS])
                            login_info = '   >>>当前用户：<%s> %s' % (PART, user)
                            self.parent.setWindowTitle(self.parent.windowTitle()[:8] + login_info)
                            self.parent.tabWidget.setCurrentIndex(0)
                        else:
                            QMessageBox.warning(self, '输入错误', '密码输入错误！')
                            self.show()
                    else:
                        QMessageBox.warning(self, '输入错误', '无该用户！')
                        self.show()
                except Exception as e:
                    user_info.log2txt('更换用户时发生错误：<{}>'.format(e))
        else:
            self.show()
