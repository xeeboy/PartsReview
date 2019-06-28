from mainform import *
from ui_login import Ui_Login

import sys
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QMainWindow


class Login(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.line_password.setText('54088726')
        self.line_username.setText('余西保')
        self.btn_login.clicked.connect(self.login)
        self.btn_quit.clicked.connect(sys.exit)
        self.show()

    def login(self):
        USERNAME, _password = self.line_username.text(), self.line_password.text()
        if USERNAME and _password:
            db = MysqlDb()
            with db:
                sql = "select 密码,部门,邮箱 from 用户 where 用户名='%s'" % USERNAME
                rst = db.get_rst(sql)
                _PARTS = db.get_rst('select 部门 from 部门')
            if rst and rst[0]['密码'] == _password:
                PART = rst[0]['部门']
                EMAIL = rst[0]['邮箱']
                user_info._init()
                user_info.set_value('USERNAME', USERNAME)
                user_info.set_value('PART', PART)
                user_info.set_value('EMAIL', EMAIL)
                user_info.set_value('PARTS', [p['部门'] for p in _PARTS])
                main_win.showMaximized()  # login success then transfer to Main Form and close login form
                main_win.setWindowTitle(main_win.windowTitle() + '   >>>当前用户：<%s> %s' % (PART, USERNAME))
                self.close()
            else:
                self.show_msg('warning', 'Error', '用户名或密码错误!')
        else:
            self.show_msg('information', 'Tips', '用户名密码不能留空!')

    def show_msg(self, level, win_title, text):
        eval('QMessageBox.%s(self, win_title, text)' % level)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    main_win = MainForm()
    sys.exit(app.exec_())
