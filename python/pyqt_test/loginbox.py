# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginbox.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(402, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoginForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 190, 251, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout.addWidget(self.login_button)
        self.cancel_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.username_input = QtWidgets.QLineEdit(LoginForm)
        self.username_input.setGeometry(QtCore.QRect(130, 60, 201, 28))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(LoginForm)
        self.password_input.setGeometry(QtCore.QRect(130, 110, 201, 28))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.legalese_checkbox = QtWidgets.QCheckBox(LoginForm)
        self.legalese_checkbox.setGeometry(QtCore.QRect(130, 160, 141, 21))
        self.legalese_checkbox.setObjectName("legalese_checkbox")
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setGeometry(QtCore.QRect(60, 70, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LoginForm)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 58, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)
        LoginForm.setTabOrder(self.username_input, self.password_input)
        LoginForm.setTabOrder(self.password_input, self.legalese_checkbox)
        LoginForm.setTabOrder(self.legalese_checkbox, self.login_button)
        LoginForm.setTabOrder(self.login_button, self.cancel_button)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.login_button.setText(_translate("LoginForm", "Login"))
        self.cancel_button.setText(_translate("LoginForm", "Cancel"))
        self.legalese_checkbox.setText(_translate("LoginForm", "Agree to Legalese"))
        self.label.setText(_translate("LoginForm", "Username"))
        self.label_2.setText(_translate("LoginForm", "Password"))
