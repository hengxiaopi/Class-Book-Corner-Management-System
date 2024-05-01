# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 330)
        Form.setMinimumSize(QtCore.QSize(500, 330))
        Form.setMaximumSize(QtCore.QSize(500, 330))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setGeometry(QtCore.QRect(400, 290, 91, 31))
        self.ok.setObjectName("ok")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 100, 471, 201))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(90, 20, 401, 61))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.retranslateUi(Form)
        self.ok.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "班级图书角管理系统"))
        self.ok.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "指导教师：谢威老师\n"
"创 作  人：刘宇辰\n"
"班　　级：2018级5班\n"
"组　　名：知识守护者\n"
"组　　员：黄昭恺、吴显彬、郭嘉煜、陈厚任、谢浚锴、邓彦弘、陈珞昕\n"
"我们小组发现每个班级都有图书角，但是却没有像图书馆一样的管理系统，于是我们编写了这个系统，便于各个班级管理自己的图书角。\n"
"\n"
"\n"
"\n"
"                                                                        演武小学2018级5班\"知识守护者\"小组赠"))
        self.title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:32pt; color:#5500ff;\">班级图书角管理系统</span></p></body></html>"))

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())