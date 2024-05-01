# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import sys,os,tkinter as tk,datetime
title="班级图书角管理系统"
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

def setTableItemText(tableWidget:QtWidgets.QTableWidget,row,col,text):
    item=QtWidgets.QTableWidgetItem(text)
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    tableWidget.setItem(row-1,col-1,item)

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 450)
        MainWindow.setMinimumSize(710,200)
        MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 901, 61))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.books_table = QtWidgets.QTableWidget(self.centralwidget)
        self.books_table.setGeometry(QtCore.QRect(10, 120, 881, 321))
        self.books_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.books_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.books_table.setObjectName("books_table")
        self.books_table.setColumnCount(12)
        for i in range(12):
            self.books_table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())
        self.load_data()
        self.books_table.verticalHeader().setVisible(False)
        self.books_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.books_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.books_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.books_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.books_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.book_man = QtWidgets.QGroupBox(self.centralwidget)
        self.book_man.setGeometry(QtCore.QRect(10, 50, 451, 61))
        self.book_man.setObjectName("book_man")
        self.add_button = QtWidgets.QPushButton(self.book_man)
        self.add_button.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.add_button.clicked.connect(self.add_book)
        self.add_button.setObjectName("add_button")
        self.del_button = QtWidgets.QPushButton(self.book_man)
        self.del_button.setGeometry(QtCore.QRect(120, 20, 101, 31))
        self.del_button.clicked.connect(self.del_book)
        self.del_button.setObjectName("del_button")
        self.edit_button = QtWidgets.QPushButton(self.book_man)
        self.edit_button.setGeometry(QtCore.QRect(230, 20, 101, 31))
        self.edit_button.clicked.connect(self.edit_book)
        self.edit_button.setObjectName("edit_button")
        self.find_button = QtWidgets.QPushButton(self.book_man)
        self.find_button.setGeometry(QtCore.QRect(340, 20, 101, 31))
        self.find_button.clicked.connect(self.find_book)
        self.find_button.setObjectName("find_button")
        self.borrow_man = QtWidgets.QGroupBox(self.centralwidget)
        self.borrow_man.setGeometry(QtCore.QRect(470, 50, 231, 61))
        self.borrow_man.setObjectName("borrow_man")
        self.borrow_button = QtWidgets.QPushButton(self.borrow_man)
        self.borrow_button.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.borrow_button.clicked.connect(self.borrow_book)
        self.borrow_button.setObjectName("borrow_button")
        self.return_button = QtWidgets.QPushButton(self.borrow_man)
        self.return_button.setGeometry(QtCore.QRect(120, 20, 101, 31))
        self.return_button.clicked.connect(self.return_book)
        self.return_button.setObjectName("return_button")
        self.about_button=QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setGeometry(QtCore.QRect(710, 70, 101, 31))
        self.about_button.clicked.connect(self.about_system)
        self.about_button.setText("关于此系统")
        self.find_lineedit=QtWidgets.QLineEdit(self.centralwidget)
        self.find_lineedit.setGeometry(QtCore.QRect(10,120,881,25))
        self.find_lineedit.setVisible(False)
        self.find_lineedit.textChanged.connect(self.find_book)
        self.find_lineedit.setPlaceholderText("输入想要查找的内容，可根据书籍所有信息查找")
        self.close_lineedit=QtWidgets.QPushButton(self.centralwidget)
        self.close_lineedit.setGeometry(QtCore.QRect(867,123,21,21))
        self.close_lineedit.setIcon(QtGui.QIcon("close.png"))
        self.close_lineedit.setStyleSheet("QPushButton {\n"
"        border: none;\n"
"        padding: 0px;\n"
"    }")
        self.close_lineedit.setVisible(False)
        self.close_lineedit.clicked.connect(self.close_find_book)
        self.find_flag=False
        self.flush=QtCore.QTimer(self)
        self.flush.timeout.connect(self.refresh_widget)
        self.flush.start(100)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def refresh_widget(self):
        width=MainWindow.width()
        height=MainWindow.height()
        if self.find_flag:
            self.books_table.setGeometry(QtCore.QRect(10, 145, width-20, height-155))
        else:
            self.books_table.setGeometry(QtCore.QRect(10, 120, width-20, height-130))
        self.title.setGeometry(QtCore.QRect(0, 0, width, 61))
        self.find_lineedit.setGeometry(QtCore.QRect(10,120,width-20,25))
        self.close_lineedit.setGeometry(QtCore.QRect(width-33,123,21,21))

    def save_data(self):
        data=[]
        with open("book_data.txt","w",encoding="utf-8") as f:
            for row in range(self.books_table.rowCount()):
                data.append([])
                for col in range(self.books_table.columnCount()-1):
                    data[row].append(self.books_table.item(row,col).text())
            f.write(str(data))

    def load_data(self):
        with open("book_data.txt","r",encoding="utf-8") as f:
            data=eval(f.read())
        self.books_table.setRowCount(len(data))
        for row in range(len(data)):
            for col in range(len(data[row])):
                setTableItemText(self.books_table,row+1,col+1,data[row][col])
            if data[row][-1]!="无":
                for date in data[row][-1].split("\n"):
                    year,month,day=date.split("/")
                    year=int(year)
                    month=int(month)
                    day=int(day)
                    borrow_date=datetime.date(year,month,day)
                    today=datetime.datetime.now().date()
                    if today<=borrow_date:
                        setTableItemText(self.books_table,row+1,12,'否')
                    else:
                        setTableItemText(self.books_table,row+1,12,'是')
            else:
                setTableItemText(self.books_table,row+1,12,"无")

    def add_book(self):
        self.add_button.setEnabled(False)
        open("add_info.txt","w",encoding="utf-8").write("preparing")
        os.system("start add_book.exe")
        while open("add_info.txt","r",encoding="utf-8").read()=="preparing" or open("add_info.txt","r",encoding="utf-8").read()=="":
            QtWidgets.QApplication.processEvents()
        new_book_info=eval(open("add_info.txt","r",encoding="utf-8").read())
        if new_book_info:
            self.books_table.setRowCount(self.books_table.rowCount()+1)
            for col in range(7):
                setTableItemText(self.books_table,self.books_table.rowCount(),col+1,new_book_info[col])
            for col in range(5):
                setTableItemText(self.books_table,self.books_table.rowCount(),col+8,["否","无","无","无","无"][col])
            self.save_data()
        self.add_button.setEnabled(True)

    def del_book(self):
        self.del_button.setEnabled(False)
        if self.books_table.selectedItems():
            window=tk.Tk()
            window.withdraw()
            if self.books_table.item(self.books_table.row(self.books_table.selectedItems()[0]),7).text()=="否":
                if messagebox.askquestion(title,"确认要删除这本书吗")=="yes":
                    self.books_table.removeRow(self.books_table.row(self.books_table.selectedItems()[0]))
                    self.save_data()
            else:
                messagebox.showwarning(title,"有同学借阅了此图书，归还图书后才能删除")
        else:
            window=tk.Tk()
            window.withdraw()
            messagebox.showwarning(title,"请先选择要删除的图书")
        self.del_button.setEnabled(True)

    def edit_book(self):
        if self.books_table.selectedItems():
            self.edit_button.setEnabled(False)
            row=self.books_table.row(self.books_table.selectedItems()[0])
            info=[self.books_table.item(row,col).text() for col in range(7)]
            with open("edit_info.txt","w",encoding="utf-8") as f:
                f.write(str(info))
            os.system("start edit_book.exe")
            file=open("edit_info.txt","r",encoding="utf-8").read()
            while file!="" and eval(file)==info:
                QtWidgets.QApplication.processEvents()
                file=open("edit_info.txt","r",encoding="utf-8").read()
            with open("edit_info.txt","r",encoding="utf-8") as f:
                edit_info=f.read()
                if edit_info!="None":
                    edit_info=eval(edit_info)
                    for col in range(6):
                        setTableItemText(self.books_table,row+1,col+2,edit_info[col])
            self.edit_button.setEnabled(True)
            self.save_data()
        else:
            window=tk.Tk()
            window.withdraw()
            messagebox.showwarning(title,"请先选择要编辑的图书")

    def find_book(self):
        if self.find_lineedit.isVisible():
            self.load_data()
            if self.find_lineedit.text():
                remove_rows=[]
                for row in range(self.books_table.rowCount()):
                    flag=False
                    for col in range(self.books_table.columnCount()):
                        if self.find_lineedit.text() in self.books_table.item(row,col).text():
                            flag=True
                            break
                    if not flag:
                        remove_rows.append(row)
                for row in range(len(remove_rows)):
                    self.books_table.removeRow(remove_rows[row]-row)
            self.books_table.clearSelection()
        else:
            self.save_data()
            self.find_button.setEnabled(False)
            self.find_lineedit.clear()
            self.find_lineedit.setVisible(True)
            self.close_lineedit.setVisible(True)
            self.find_flag=True

    def close_find_book(self):
        self.find_lineedit.setVisible(False)
        self.close_lineedit.setVisible(False)
        self.load_data()
        self.find_flag=False
        self.find_button.setEnabled(True)

    def borrow_book(self):
        if self.books_table.selectedItems():
            row=self.books_table.row(self.books_table.selectedItems()[0])
            self.borrow_button.setEnabled(False)
            with open("borrow_info.txt","w",encoding="utf-8") as f:
                f.write(str([self.books_table.item(row,i).text() for i in range(7)]))
            os.system("start borrow_book.exe")
            while open("borrow_info.txt","r",encoding="utf-8").read()==str([self.books_table.item(self.books_table.row(self.books_table.selectedItems()[0]),i).text() for i in range(7)]) or open("borrow_info.txt","r",encoding="utf-8").read()=="":
                QtWidgets.QApplication.processEvents()
            with open("borrow_info.txt","r",encoding="utf-8") as f:
                stu_name=f.read()
                if stu_name!="None":
                    setTableItemText(self.books_table,row+1,7,str(int(self.books_table.item(row,6).text())-1))
                    if self.books_table.item(row,7).text()=="否":
                        row+=1
                        setTableItemText(self.books_table,row,8,"是")
                        setTableItemText(self.books_table,row,9,stu_name)
                        now=datetime.datetime.now()
                        setTableItemText(self.books_table,row,10,now.strftime("%Y/%m/%d"))
                        setTableItemText(self.books_table,row,11,(now+datetime.timedelta(weeks=2)).strftime("%Y/%m/%d"))
                        setTableItemText(self.books_table,row,12,"否")
                    else:
                        setTableItemText(self.books_table,row+1,9,self.books_table.item(row,8).text()+"\n"+stu_name)
                        now=datetime.datetime.now()
                        setTableItemText(self.books_table,row+1,10,self.books_table.item(row,9).text()+"\n"+now.strftime("%Y/%m/%d"))
                        setTableItemText(self.books_table,row+1,11,self.books_table.item(row,10).text()+"\n"+(now+datetime.timedelta(weeks=2)).strftime("%Y/%m/%d"))
                        setTableItemText(self.books_table,row+1,12,self.books_table.item(row,11).text()+"\n"+"否")
            self.borrow_button.setEnabled(True)
            self.save_data()
        else:
            window=tk.Tk()
            window.withdraw()
            messagebox.showwarning(title,"请先选择要借阅的图书")

    def return_book(self):
        if self.books_table.selectedItems():
            row=self.books_table.row(self.books_table.selectedItems()[0])
            if self.books_table.item(row,7).text()=="否":
                window=tk.Tk()
                window.withdraw()
                messagebox.showwarning(title,"此图书没有被借阅")
                return
            self.return_button.setEnabled(False)
            info=[self.books_table.item(row,i).text() for i in range(7)]
            info.append(self.books_table.item(row,8).text().split("\n"))
            info=str(info)
            with open("return_info.txt","w",encoding="utf-8") as f:
                f.write(info)
            os.system("start return_book.exe")
            while open("return_info.txt","r",encoding="utf-8").read()==info or open("return_info.txt","r",encoding="utf-8").read()=="":
                QtWidgets.QApplication.processEvents()
            with open("return_info.txt","r",encoding="utf-8") as f:
                stu_name=f.read()
                if stu_name!="None":
                    name_lst=self.books_table.item(row,8).text().split("\n")
                    index=name_lst.index(stu_name)
                    name_lst.remove(stu_name)
                    setTableItemText(self.books_table,row+1,7,str(int(self.books_table.item(row,6).text())+1))
                    if len(name_lst)==0:
                        for col in range(5):
                            setTableItemText(self.books_table,row+1,col+8,["否","无","无","无","无"][col])
                    else:
                        setTableItemText(self.books_table,row+1,9,"\n".join(name_lst))
                        for col in range(9,12):
                            lst=self.books_table.item(row,col).text().split("\n")
                            del lst[index]
                            setTableItemText(self.books_table,row+1,col+1,"\n".join(lst))
            self.return_button.setEnabled(True)
            self.save_data()
        else:
            window=tk.Tk()
            window.withdraw()
            messagebox.showwarning(title,"请先选择要归还的图书")

    def about_system(self):
        os.system("start about.exe")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", title))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">%s</span></p></body></html>"%title))
        self.books_table.setSortingEnabled(True)
        item = self.books_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "编号"))
        item = self.books_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "分类"))
        item = self.books_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "书名"))
        item = self.books_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "作者"))
        item = self.books_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "出版社"))
        item = self.books_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "出版日期"))
        item = self.books_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "剩余数量"))
        item = self.books_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "是否被借阅"))
        item = self.books_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "借阅人"))
        item = self.books_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "借阅日期"))
        item = self.books_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "应归还日期"))
        item = self.books_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "是否超时"))
        self.book_man.setTitle(_translate("MainWindow", "图书管理"))
        self.add_button.setText(_translate("MainWindow", "图书添加"))
        self.del_button.setText(_translate("MainWindow", "图书删除"))
        self.edit_button.setText(_translate("MainWindow", "图书编辑"))
        self.find_button.setText(_translate("MainWindow", "图书查找"))
        self.borrow_man.setTitle(_translate("MainWindow", "借阅管理"))
        self.borrow_button.setText(_translate("MainWindow", "图书借阅"))
        self.return_button.setText(_translate("MainWindow", "图书归还"))

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
