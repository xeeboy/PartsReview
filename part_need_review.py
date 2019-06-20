# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part_need_review.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QCheckBox, QPushButton
import sys
from getdb import AccDb

db = AccDb()
with db:
    rst = db.get_rst('SELECT 部门 from 部门')
PARTS = [item[0] for item in rst]


class Ui_parts_need_review(object):
    def setupUi(self, parts_need_review):
        parts_need_review.setObjectName("parts_need_review")
        parts_need_review.resize(262, 304)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/user.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        parts_need_review.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(parts_need_review)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.groupBox = QtWidgets.QGroupBox(parts_need_review)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)  # add item into groupBox
        for part in PARTS:
            check = QCheckBox(part)
            check.setObjectName(part)
            self.verticalLayout_4.addWidget(check)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.btn_save = QPushButton('保存')
        self.verticalLayout.addWidget(self.btn_save)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(parts_need_review)
        self.btn_save.clicked.connect(self.parts_need)
        QtCore.QMetaObject.connectSlotsByName(parts_need_review)

    def retranslateUi(self, parts_need_review):
        _translate = QtCore.QCoreApplication.translate
        parts_need_review.setWindowTitle(_translate("parts_need_review", "选择需参与的部门"))
        self.groupBox.setTitle(_translate("parts_need_review", "参与部门"))

    def parts_need(self):
        check_list =  self.groupBox.findChildren(QCheckBox)
        parts = ','.join([check.objectName() for check in check_list if check.isChecked()])
        print(parts)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_parts_need_review()
    frm = QtWidgets.QDialog()
    ui.setupUi(frm)
    frm.show()
    sys.exit(app.exec_())
