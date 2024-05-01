# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import sys,tkinter as tk
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 330)
        Form.setMinimumSize(QtCore.QSize(400, 330))
        Form.setMaximumSize(QtCore.QSize(400, 330))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 9, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.label_2.setObjectName("label_2")
        self.stu_name = QtWidgets.QLineEdit(Form)
        self.stu_name.setGeometry(QtCore.QRect(70, 10, 321, 31))
        self.stu_name.setObjectName("stu_name")
        self.name = QtWidgets.QLabel(Form)
        self.name.setGeometry(QtCore.QRect(10, 140, 381, 31))
        self.name.setObjectName("name")
        self.author = QtWidgets.QLabel(Form)
        self.author.setGeometry(QtCore.QRect(10, 170, 381, 31))
        self.author.setObjectName("author")
        self.publisher = QtWidgets.QLabel(Form)
        self.publisher.setGeometry(QtCore.QRect(10, 200, 381, 31))
        self.publisher.setObjectName("publisher")
        self.date = QtWidgets.QLabel(Form)
        self.date.setGeometry(QtCore.QRect(10, 230, 381, 31))
        self.date.setObjectName("date")
        self.count = QtWidgets.QLabel(Form)
        self.count.setGeometry(QtCore.QRect(10, 260, 381, 31))
        self.count.setObjectName("count")
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setGeometry(QtCore.QRect(120, 290, 81, 31))
        self.ok.clicked.connect(self.commit_info)
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(210, 290, 81, 31))
        self.cancel.setObjectName("cancel")
        self.number = QtWidgets.QLabel(Form)
        self.number.setGeometry(QtCore.QRect(10, 80, 381, 31))
        self.number.setObjectName("number")
        self.classify = QtWidgets.QLabel(Form)
        self.classify.setGeometry(QtCore.QRect(10, 110, 381, 31))
        self.classify.setObjectName("classify")
        self.finish=False

        self.retranslateUi(Form)
        self.cancel.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.form=Form

    def commit_info(self):
        if self.stu_name.text():
            with open("borrow_info.txt","w",encoding="utf-8") as f:
                f.write(self.stu_name.text())
            self.finish=True
            self.form.close()
        else:
            window=tk.Tk()
            window.withdraw()
            messagebox.showwarning("班级图书角管理系统","请填写借阅人姓名")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        data=eval(open("borrow_info.txt","r",encoding="utf-8").read())
        Form.setWindowTitle(_translate("Form", "班级图书角管理系统"))
        self.label.setText(_translate("Form", "借  阅 人："))
        self.label_2.setText(_translate("Form", "书籍信息："))
        self.number.setText(_translate("Form", "编　　号："+data[0]))
        self.classify.setText(_translate("Form", "分　　类："+data[1]))
        self.name.setText(_translate("Form", "书　　名："+data[2]))
        self.author.setText(_translate("Form", "作　　者："+data[3]))
        self.publisher.setText(_translate("Form", "出  版 社："+data[4]))
        self.date.setText(_translate("Form", "出版日期："+data[5]))
        self.count.setText(_translate("Form", "数　　量："+data[6]))
        self.ok.setText(_translate("Form", "确定"))
        self.cancel.setText(_translate("Form", "取消"))

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    if not ui.finish:
        open("borrow_info.txt","w",encoding="utf-8").write("None")