# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled4.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 542)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Think/.designer/backup/02b616f2c3b0aa86ef0313f38a4bbe13.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 440, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 40, 191, 291))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-image: url(:/bbb/02b616f2c3b0aa86ef0313f38a4bbe13.jpg);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(310, 10, 191, 291))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 440, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 370, 54, 12))
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(160, 180, 301, 191))
        self.graphicsView.setStyleSheet("border-image: url(:/bbb/02b616f2c3b0aa86ef0313f38a4bbe13.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 614, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.dbend = QtWidgets.QToolBar(MainWindow)
        self.dbend.setMouseTracking(False)
        self.dbend.setInputMethodHints(QtCore.Qt.ImhDate)
        self.dbend.setObjectName("dbend")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.dbend)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAcceptDrops(True)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setCheckable(True)
        self.action.setChecked(True)
        self.action.setObjectName("action")
        self.action4444 = QtWidgets.QAction(MainWindow)
        self.action4444.setCheckable(True)
        self.action4444.setObjectName("action4444")
        self.menu.addAction(self.action)
        self.menuBar.addAction(self.menu.menuAction())
        self.dbend.addSeparator()
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.action.changed.connect(MainWindow.slot1)
        self.menuBar.triggered['QAction*'].connect(MainWindow.close)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "close"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff;\">顶顶顶顶顶顶</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "show"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.dbend.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action.setText(_translate("MainWindow", "11111"))
        self.action.setToolTip(_translate("MainWindow", "<html><head/><body><p>111111111111111</p></body></html>"))
        self.action4444.setText(_translate("MainWindow", "4444"))
        self.action4444.setToolTip(_translate("MainWindow", "<html><head/><body><p>uuuuunj</p></body></html>"))

import aaa_rc
