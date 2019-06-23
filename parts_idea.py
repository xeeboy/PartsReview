# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idea.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from getdb import AccDb
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_partidea(object):
    def setupUi(self, partidea):
        partidea.setObjectName("partidea")
        partidea.resize(501, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/input_tablet_32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        partidea.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(partidea)
        self.label.setGeometry(QtCore.QRect(29, 49, 60, 16))
        self.label.setObjectName("label")
        self.txt_tec_part = QtWidgets.QTextEdit(partidea)
        self.txt_tec_part.setGeometry(QtCore.QRect(119, 49, 231, 74))
        self.txt_tec_part.setObjectName("txt_tec_part")
        self.label_2 = QtWidgets.QLabel(partidea)
        self.label_2.setGeometry(QtCore.QRect(29, 129, 60, 16))
        self.label_2.setObjectName("label_2")
        self.txt_pro_part = QtWidgets.QTextEdit(partidea)
        self.txt_pro_part.setGeometry(QtCore.QRect(119, 129, 231, 74))
        self.txt_pro_part.setObjectName("txt_pro_part")
        self.label_3 = QtWidgets.QLabel(partidea)
        self.label_3.setGeometry(QtCore.QRect(29, 209, 60, 16))
        self.label_3.setObjectName("label_3")
        self.txt_qc_part = QtWidgets.QTextEdit(partidea)
        self.txt_qc_part.setGeometry(QtCore.QRect(119, 209, 231, 73))
        self.txt_qc_part.setObjectName("txt_qc_part")
        self.label_4 = QtWidgets.QLabel(partidea)
        self.label_4.setGeometry(QtCore.QRect(29, 288, 84, 16))
        self.label_4.setObjectName("label_4")
        self.txt_tec_support = QtWidgets.QTextEdit(partidea)
        self.txt_tec_support.setGeometry(QtCore.QRect(119, 288, 231, 74))
        self.txt_tec_support.setObjectName("txt_tec_support")
        self.label_5 = QtWidgets.QLabel(partidea)
        self.label_5.setGeometry(QtCore.QRect(29, 368, 60, 16))
        self.label_5.setObjectName("label_5")
        self.txt_general_m = QtWidgets.QTextEdit(partidea)
        self.txt_general_m.setGeometry(QtCore.QRect(119, 368, 231, 74))
        self.txt_general_m.setObjectName("txt_general_m")
        self.gpb_deal = QtWidgets.QGroupBox(partidea)
        self.gpb_deal.setGeometry(QtCore.QRect(370, 40, 111, 241))
        self.gpb_deal.setObjectName("gpb_deal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gpb_deal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chk_devi_release = QtWidgets.QCheckBox(self.gpb_deal)
        self.chk_devi_release.setObjectName("chk_devi_release")
        self.verticalLayout.addWidget(self.chk_devi_release)
        self.chk_rework = QtWidgets.QCheckBox(self.gpb_deal)
        self.chk_rework.setObjectName("chk_rework")
        self.verticalLayout.addWidget(self.chk_rework)
        self.chk_downgrade = QtWidgets.QCheckBox(self.gpb_deal)
        self.chk_downgrade.setObjectName("chk_downgrade")
        self.verticalLayout.addWidget(self.chk_downgrade)
        self.chk_direc_sales = QtWidgets.QCheckBox(self.gpb_deal)
        self.chk_direc_sales.setObjectName("chk_direc_sales")
        self.verticalLayout.addWidget(self.chk_direc_sales)
        self.chk_scrap = QtWidgets.QCheckBox(self.gpb_deal)
        self.chk_scrap.setObjectName("chk_scrap")
        self.verticalLayout.addWidget(self.chk_scrap)
        self.btn_deal_method = QtWidgets.QPushButton(self.gpb_deal)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/pass_to_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_deal_method.setIcon(icon1)
        self.btn_deal_method.setObjectName("btn_deal_method")
        self.verticalLayout.addWidget(self.btn_deal_method)
        self.btn_save_idea = QtWidgets.QPushButton(partidea)
        self.btn_save_idea.setGeometry(QtCore.QRect(160, 470, 72, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_idea.sizePolicy().hasHeightForWidth())
        self.btn_save_idea.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Save_32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_idea.setIcon(icon2)
        self.btn_save_idea.setObjectName("btn_save_idea")
        self.btn_sign_name = QtWidgets.QPushButton(partidea)
        self.btn_sign_name.setGeometry(QtCore.QRect(290, 470, 72, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sign_name.sizePolicy().hasHeightForWidth())
        self.btn_sign_name.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/dealidea.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sign_name.setIcon(icon3)
        self.btn_sign_name.setObjectName("btn_sign_name")

        self.retranslateUi(partidea)
        QtCore.QMetaObject.connectSlotsByName(partidea)
        partidea.setTabOrder(self.txt_tec_part, self.txt_pro_part)
        partidea.setTabOrder(self.txt_pro_part, self.txt_qc_part)
        partidea.setTabOrder(self.txt_qc_part, self.txt_tec_support)
        partidea.setTabOrder(self.txt_tec_support, self.txt_general_m)
        partidea.setTabOrder(self.txt_general_m, self.chk_devi_release)
        partidea.setTabOrder(self.chk_devi_release, self.chk_rework)
        partidea.setTabOrder(self.chk_rework, self.chk_downgrade)
        partidea.setTabOrder(self.chk_downgrade, self.chk_direc_sales)
        partidea.setTabOrder(self.chk_direc_sales, self.chk_scrap)
        partidea.setTabOrder(self.chk_scrap, self.btn_save_idea)
        partidea.setTabOrder(self.btn_save_idea, self.btn_sign_name)

    def retranslateUi(self, partidea):
        _translate = QtCore.QCoreApplication.translate
        partidea.setWindowTitle(_translate("partidea", "意见输入"))
        self.label.setText(_translate("partidea", "技术部意见"))
        self.label_2.setText(_translate("partidea", "工艺部意见"))
        self.label_3.setText(_translate("partidea", "质量部意见"))
        self.label_4.setText(_translate("partidea", "技术支持部意见"))
        self.label_5.setText(_translate("partidea", "总经理意见"))
        self.gpb_deal.setTitle(_translate("partidea", "选择处置方式"))
        self.chk_devi_release.setText(_translate("partidea", "偏差放行"))
        self.chk_rework.setText(_translate("partidea", "返工"))
        self.chk_downgrade.setText(_translate("partidea", "降级"))
        self.chk_direc_sales.setText(_translate("partidea", "定向销售"))
        self.chk_scrap.setText(_translate("partidea", "报废"))
        self.btn_deal_method.setToolTip(_translate("partidea", "<html><head/><body><p><span style=\" font-style:italic; color:#55ff00;\">不在上述列表中的处置方式可手动输入</span></p></body></html>"))
        self.btn_deal_method.setText(_translate("partidea", "Add"))
        self.btn_save_idea.setText(_translate("partidea", "保存"))
        self.btn_sign_name.setToolTip(_translate("partidea", "<html><head/><body><p><span style=\" font-size:8pt; font-style:italic; color:#0055ff;\">在意见输入框末尾添加</span></p></body></html>"))
        self.btn_sign_name.setText(_translate("partidea", "签名"))


class IdeaDialog(QtWidgets.QDialog, Ui_partidea):
    def __init__(self, parent, department, _unpass_id):
        super().__init__(parent)
        ctlname_zh = dict(txt_tec_part='技术部', txt_pro_part='工艺部', txt_qc_part='质量部', txt_tec_support='技术支持部',
                        txt_general_m='总经办')
        self.parent = parent
        self.deal_id = _unpass_id
        self.setupUi(self)
        for ctl in self.findChildren(QtWidgets.QTextEdit):
            if ctlname_zh[ctl.objectName()] == department:
                ctl.setEnabled(True)
            else:
                ctl.setEnabled(False)
        self.btn_save_idea.clicked.connect(self.saveidea)
        self.btn_sign_name.clicked.connect(self.sign)
        self.btn_deal_method.clicked.connect(self.addmethods)

    def saveidea(self):
        # db = AccDb()
        # with db:
        #     sql = "update 不合格品登记 set "
        pass

    def sign(self):
        pass

    def addmethods(self):
        pass
