# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\JHU\课程\data design\Assignment_display.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, -20, 711, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("e:\\JHU\\课程\\data design\\background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 611, 411))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane{\n"
"min-width:70px;\n"
"min-height:25px;\n"
"border-top: 2px solid;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"\n"
"color: white;\n"
"\n"
"font:15px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"color: #4796f0;\n"
"\n"
"font:15px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"border-bottom: 2px solid;\n"
"\n"
"border-color: #4796f0;\n"
"\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 151, 21))
        self.label_2.setStyleSheet("color:white;\n"
"font:15px \"Microsoft YaHei\";")
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(190, 60, 131, 22))
        self.spinBox.setStyleSheet("background-color: rgb(96,104,132);\n"
"font-family: 微软雅黑;\n"
"color:white\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 151, 21))
        self.label_3.setStyleSheet("color:white;\n"
"font:15px \"Microsoft YaHei\";")
        self.label_3.setObjectName("label_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_2.setGeometry(QtCore.QRect(190, 100, 131, 22))
        self.spinBox_2.setStyleSheet("background-color: rgb(96,104,132);\n"
"font-family: 微软雅黑;\n"
"color:white\n"
"")
        self.spinBox_2.setObjectName("spinBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(30, 170, 551, 181))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_1)
        self.graphicsView.setGeometry(QtCore.QRect(70, 20, 471, 291))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setStyleSheet("border-radius:10px;")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 320, 281, 41))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setAcceptDrops(True)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background:rgb(255, 255, 255, 60);\n"
"    color:white;\n"
"    border-radius: 8px;\n"
"    font-family: 微软雅黑;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover{                    \n"
"    background:rgb(255, 255, 255, 100);\n"
"}\n"
"QPushButton:pressed{\n"
"    background: darkgray;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_1, "")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 20, 16, 16))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background:#6C6C6C;\n"
"    color:white;\n"
"    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#9D9D9D;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 1px solid #3C3C3C!important;\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 20, 16, 16))
        self.pushButton_7.setStatusTip("")
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background:green;\n"
"    color:white;\n"
"    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#7bcd68;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 1px solid #3C3C3C!important;\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(620, 20, 16, 16))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background:#CE0000;\n"
"    color:white;\n"
"    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#FF2D2D;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 1px solid #3C3C3C!important;\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(530, 20, 16, 16))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background:#abac30;\n"
"    color:white;\n"
"    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
"}\n"
"QPushButton:hover{\n"
"    background:yellow;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 1px solid #3C3C3C!important;\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Number of Patients"))
        self.label_3.setText(_translate("MainWindow", "Number of Doctors"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Input"))
        self.pushButton_3.setText(_translate("MainWindow", "Output Chart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Output"))
        self.pushButton_5.setToolTip(_translate("MainWindow", "最小化"))
        self.pushButton_7.setToolTip(_translate("MainWindow", "最大化及还原"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "关闭程序"))
        self.pushButton_8.setToolTip(_translate("MainWindow", "重启程序"))