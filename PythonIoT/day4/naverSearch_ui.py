# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'naverSearch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 412)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 421, 71))
        self.groupBox.setFlat(False)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 61, 22))
        self.txtSearchWord = QLineEdit(self.groupBox)
        self.txtSearchWord.setObjectName(u"txtSearchWord")
        self.txtSearchWord.setGeometry(QRect(80, 20, 251, 32))
        self.btnSearch = QPushButton(self.groupBox)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(340, 20, 71, 30))
        self.tblResult = QTableWidget(self.centralwidget)
        self.tblResult.setObjectName(u"tblResult")
        self.tblResult.setGeometry(QRect(10, 70, 431, 311))
        # MainWindow.setCentralWidget(self.centralwidget)
        self.stsResult = QStatusBar(MainWindow)
        self.stsResult.setObjectName(u"stsResult")
        # MainWindow.setStatusBar(self.stsResult)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ub124\uc774\ubc84 \uac80\uc0c9", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uc5b4 :", None))
        self.btnSearch.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
    # retranslateUi

