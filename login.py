# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sys
import getdb
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow


class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(408, 246)
        Form.setMaximumSize(QtCore.QSize(408, 246))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/login.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.form = Form

        self.lbl_title = QtWidgets.QLabel(Form)
        self.lbl_title.setGeometry(QtCore.QRect(30, 20, 351, 31))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(110, 70, 191, 81))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.gridLayout = QtWidgets.QGridLayout()

        self.line_username = QtWidgets.QLineEdit(self.widget)
        font.setBold(False)
        font.setFamily("微软雅黑")
        font.setWeight(50)
        font.setPointSize(10)
        self.line_username.setFont(font)
        self.line_username.setPlaceholderText('用户名')  # 背景灰色提示文字
        self.gridLayout.addWidget(self.line_username, 0, 2, 1, 1)

        self.line_password = QtWidgets.QLineEdit(self.widget)
        self.line_password.setFont(font)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setPlaceholderText('密码')
        self.gridLayout.addWidget(self.line_password, 1, 2, 1, 1)

        self.lbl_password = QtWidgets.QLabel(self.widget)
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_password.setFont(font)
        self.lbl_password.setPixmap(QtGui.QPixmap("icons/password24px.ico"))
        self.gridLayout.addWidget(self.lbl_password, 1, 0, 1, 1)
        self.lbl_username = QtWidgets.QLabel(self.widget)

        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_username.setFont(font)
        self.lbl_username.setPixmap(QtGui.QPixmap("icons/user24px.ico"))
        self.gridLayout.addWidget(self.lbl_username, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(145, 180, 150, 24))  # 调整button组的位置
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.btn_login = QtWidgets.QPushButton(self.splitter)  # 在splitter里画button

        font.setFamily("Arial Rounded MT Bold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/confirm128px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_login.setIcon(icon1)
        self.btn_login.setObjectName("btn_login")
        self.btn_quit = QtWidgets.QPushButton(self.splitter)

        self.btn_quit.setFont(font)
        self.btn_quit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/quit128px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_quit.setIcon(icon2)
        self.btn_quit.setObjectName("btn_quit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.line_username, self.line_password)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "User Login"))
        self.lbl_title.setText(_translate("Form", "不合格品评审系统"))
        self.btn_login.setText(_translate("Form", "登录"))
        self.btn_login.setShortcut(_translate("Form", "Return"))
        self.btn_quit.setText(_translate("Form", "关闭"))
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
                # TODO show mainform
                self.form.close()
            else:
                self.show_msg('warning', 'Error', '用户名或密码错误!')
        else:
            self.show_msg('information', 'Tips', '用户名密码不能留空!')

    def show_msg(self, level, win_title, text):
        eval('QtWidgets.QMessageBox.%s(self.form, win_title, text)' % level)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm_login = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(frm_login)
    frm_login.show()
    sys.exit(app.exec_())
