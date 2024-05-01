# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import sys,tkinter as tk,time
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
        self.data=eval(open("edit_info.txt","r",encoding="utf-8").read())
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 9, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 61, 31))
        self.label_2.setObjectName("label_2")
        self.classify = QtWidgets.QLineEdit(Form)
        self.classify.setGeometry(QtCore.QRect(70, 50, 321, 31))
        self.classify.setText(self.data[1])
        self.classify.setObjectName("classify")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 61, 31))
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(70, 90, 321, 31))
        self.name.setText(self.data[2])
        self.name.setObjectName("name")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 61, 31))
        self.label_4.setObjectName("label_4")
        self.author = QtWidgets.QLineEdit(Form)
        self.author.setGeometry(QtCore.QRect(70, 130, 321, 31))
        self.author.setText(self.data[3])
        self.author.setObjectName("author")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 61, 31))
        self.label_5.setObjectName("label_5")
        self.publisher = QtWidgets.QLineEdit(Form)
        self.publisher.setGeometry(QtCore.QRect(70, 170, 321, 31))
        self.publisher.setText(self.data[4])
        self.publisher.setObjectName("publisher")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 61, 31))
        self.label_6.setObjectName("label_6")
        self.date = QtWidgets.QDateEdit(Form)
        self.date.setGeometry(QtCore.QRect(70, 210, 110, 31))
        year=int(self.data[5].split("/")[0])
        month=int(self.data[5].split("/")[1])
        day=int(self.data[5].split("/")[2])
        self.date.setDate(QtCore.QDate(year,month,day))
        date=time.localtime()
        self.date.setMaximumDate(QtCore.QDate(date.tm_year,date.tm_mon,date.tm_mday))
        self.date.setObjectName("date")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 61, 31))
        self.label_7.setObjectName("label_7")
        self.count = QtWidgets.QSpinBox(Form)
        self.count.setGeometry(QtCore.QRect(70, 250, 81, 31))
        self.count.setMinimum(1)
        self.count.setMaximum(10000)
        self.count.setProperty("value", self.data[6])
        self.count.setObjectName("count")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 290, 81, 31))
        self.pushButton.clicked.connect(self.commit_info)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 290, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.form=Form
        self.finish=False

    def commit_info(self):
        with open("book_data.txt","r",encoding="utf-8") as f:
            data=f.read().split("\n")
            del data[-1]
            for i in range(len(data)):
                data[i]=data[i].split()[0]
        if self.classify.text() and self.name.text() and self.author.text() and self.publisher.text():
            self.finish=True
            with open("edit_info.txt","w",encoding="utf-8") as f:
                f.write(str([self.classify.text(),self.name.text(),self.author.text(),self.publisher.text(),self.date.text(),self.count.text()]))
            self.form.close()
        else:
            window=tk.Tk()
            window.withdraw()
            messagebox.showwarning("班级图书角管理系统","请填写完整图书信息")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "班级图书角管理系统"))
        self.label.setText(_translate("Form", "编　　号：%s"%self.data[0]))
        self.label_2.setText(_translate("Form", "分　　类："))
        self.label_3.setText(_translate("Form", "书　　名："))
        self.label_4.setText(_translate("Form", "作　　者："))
        self.label_5.setText(_translate("Form", "出  版 社："))
        self.label_6.setText(_translate("Form", "出版日期："))
        self.label_7.setText(_translate("Form", "数　　量："))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    if not ui.finish:
        open("edit_info.txt","w",encoding="utf-8").write("None")