# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(789, 594)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(200, 110, 361, 286))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label.setStyleSheet(u"font-size: 30px; ")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.ed_username = QLineEdit(self.verticalLayoutWidget)
        self.ed_username.setObjectName(u"ed_username")
        self.ed_username.setStyleSheet(u"border: solid; height: 30px; border-radius: 10px; margin: 5px")

        self.horizontalLayout_2.addWidget(self.ed_username)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.ed_password = QLineEdit(self.verticalLayoutWidget)
        self.ed_password.setObjectName(u"ed_password")
        self.ed_password.setStyleSheet(u"border: solid; height: 30px; border-radius: 10px; margin: 5px")
        self.ed_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_3.addWidget(self.ed_password)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.ed_confirm_pass = QLineEdit(self.verticalLayoutWidget)
        self.ed_confirm_pass.setObjectName(u"ed_confirm_pass")
        self.ed_confirm_pass.setStyleSheet(u"border: solid; height: 30px; border-radius: 10px; margin: 5px")
        self.ed_confirm_pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_4.addWidget(self.ed_confirm_pass)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.user_radio = QRadioButton(self.verticalLayoutWidget)
        self.user_radio.setObjectName(u"user_radio")
        self.user_radio.setStyleSheet(u"color: red")

        self.verticalLayout.addWidget(self.user_radio)

        self.admin_radio = QRadioButton(self.verticalLayoutWidget)
        self.admin_radio.setObjectName(u"admin_radio")
        self.admin_radio.setStyleSheet(u"color:blue")

        self.verticalLayout.addWidget(self.admin_radio)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_confirm = QPushButton(self.verticalLayoutWidget)
        self.bt_confirm.setObjectName(u"bt_confirm")
        self.bt_confirm.setStyleSheet(u"background-color: rgb(52, 95, 235); color: white")

        self.horizontalLayout.addWidget(self.bt_confirm)

        self.bt_cancel = QPushButton(self.verticalLayoutWidget)
        self.bt_cancel.setObjectName(u"bt_cancel")
        self.bt_cancel.setStyleSheet(u"background-color: rgb(196, 20, 28); color: white;")

        self.horizontalLayout.addWidget(self.bt_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 789, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Registration", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.ed_username.setInputMask("")
        self.ed_username.setText("")
        self.ed_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.ed_password.setInputMask("")
        self.ed_password.setText("")
        self.ed_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"confirmation", None))
        self.ed_confirm_pass.setInputMask("")
        self.ed_confirm_pass.setText("")
        self.ed_confirm_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"confirm password", None))
        self.user_radio.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.admin_radio.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.bt_confirm.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.bt_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

