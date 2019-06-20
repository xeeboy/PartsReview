from ui_login import Ui_Login
from mainform import MainForm
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget, QApplication
import sys
import getdb


class Login(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.line_password.setText('54088726')
        self.line_username.setText('余西保')
        self.btn_login.clicked.connect(self.login)
        self.btn_quit.clicked.connect(sys.exit)

    def login(self):
        username, password = self.line_username.text(), self.line_password.text()
        if username and password:
            db = getdb.AccDb()
            with db:
                sql = "select 密码 from 用户 where 用户名='%s'" % username
                rst = db.get_rst(sql)
            if rst and rst[0][0] == password:
                # login success then transfer to Main Form and close login form
                main_win.showMaximized()
                self.close()
            else:
                self.show_msg('warning', 'Error', '用户名或密码错误!')
        else:
            self.show_msg('information', 'Tips', '用户名密码不能留空!')

    def show_msg(self, level, win_title, text):
        eval('QMessageBox.%s(self, win_title, text)' % level)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainForm()
    login = Login()
    login.show()
    sys.exit(app.exec_())
