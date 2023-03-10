# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snakesenza.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pygame import mixer
from kbc import kbc
import pymysql
import pandas as pd
from tkinter import ttk
import tkinter as tk
from tkinter import *


class Ui_Dialog(object):

    def __init__(self):
        self.uname = None
        self.mydb = pymysql.connect(host="127.0.0.1", port=3306,
                                    user="root", passwd="", database="quiz game")
        self.c = self.mydb.cursor()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 528)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 531))
        self.label.setStyleSheet(
            "background-image: url(:/newPrefix/h1.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("h2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 40, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: transparent;\n"
                                    "color: white;\n"
                                    "border-style: outset;\n"
                                    "border-width:2px;\n"
                                    "border-radius:10px;\n"
                                    "border-color:blue;\n"
                                    "font:bold 14px;\n"
                                    "")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 250, 111, 41))
        self.pushButton.setStyleSheet("\n"
                                      "\n"
                                      "QPushButton {\n"
                                      "background-color:#0080FF;\n"
                                      "color: white;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 14px;\n"
                                      "padding:6px;\n"
                                      "min-width:10px;\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(173,216,230);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "\n"
                                      "color:     rgb(0,0,0);\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 330, 111, 41))
        self.pushButton_2.setStyleSheet("\n"
                                        "\n"
                                        "QPushButton {\n"
                                        "background-color:#0080FF;\n"
                                        "color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:black;\n"
                                        "font:bold 14px;\n"
                                        "padding:6px;\n"
                                        "min-width:10px;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(173,216,230);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "\n"
                                        "color:     rgb(0,0,0);\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 400, 111, 41))
        self.pushButton_3.setStyleSheet("\n"
                                        "\n"
                                        "QPushButton {\n"
                                        "background-color:#0080FF;\n"
                                        "color: white;\n"
                                        "border-style: outset;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color:black;\n"
                                        "font:bold 14px;\n"
                                        "padding:6px;\n"
                                        "min-width:10px;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(173,216,230);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "\n"
                                        "color:     rgb(0,0,0);\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 140, 221, 71))
        self.textEdit_2.setStyleSheet("background-color: transparent;\n"
                                      "color: white;\n"
                                      "border-style: outset;\n"
                                      "\n"
                                      "border-radius:10px;\n"
                                      "\n"
                                      "font:bold 14px;\n"
                                      "")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog = Dialog
        mixer.init()
       # mixer.music.load('voice.mp3')
       # mixer.music.play()  # prantheis ma -1 for repeated saying

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Quiz Game"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Ravie\'; font-size:14px; font-weight:600; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; color:#0080FF;\">Quiz Game !</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Easy"))
        self.pushButton_2.setText(_translate("Dialog", "Difficult"))
        self.pushButton_3.setText(_translate("Dialog", "Score Card"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14px; font-weight:600; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#0080FF;\">Select Mode</span></p></body></html>"))
        self.pushButton.clicked.connect(self.fun)
        self.pushButton_2.clicked.connect(self.fun1)
        self.pushButton_3.clicked.connect(self.show_score)

    def fun(self):
        print(self.uname)
        self.Dialog.hide()  # dont destroy so  you can come back
        s = kbc()
        s.mode = 'easy'
        s.uname = self.uname
        #s.dur = 8
        # print(s.dur)
        s.start()

    def fun1(self):
        print(self.uname)
        self.Dialog.hide()  # dont destroy so  you can come back
        a = kbc()
        a.mode = 'difficult'
        a.uname = self.uname
        #a.dur = 15
        # print(a.dur)
        a.start()

    def show_score(self):
        try:
            self.name = []
            self.score_card = []
            self.date_time = []
            print(self.uname)

            self.c.execute(
                ' SELECT `score` FROM `score` WHERE user_name=%s', (self.uname))
            res4 = self.c.fetchall()

            for i in res4:
                l = list(i)
                self.score_card.append(l[0])
            print(self.score_card, 'xd')

            self.c.execute(
                ' SELECT `date_time` FROM `score` WHERE user_name=%s', (self.uname))
            res4 = self.c.fetchall()

            for i in res4:
                l = list(i)
                self.date_time.append(pd.to_datetime(l[0]))
            print(self.date_time, 'xd')

    ##        self.c.execute(' SELECT `user_name` FROM `score` WHERE user_name=%s',(self.uname))
    ##        res4 = self.c.fetchall()
    ##
    # for i in res4:
    ##            l = list(i)
    # self.name.append(l[0])
    # print(self.name,'xd')

            strg = f'\n           SCORE               DATE AND TIME\n'
            strg += '\n'
            for i in range(len(self.date_time)):
                strg += f'              {self.score_card[i]}                   {self.date_time[i]} \n\n '

            strg += f' Player Name: {self.uname} \n'

            strg += f' Avg Score :  {round(sum(self.score_card)/len(self.score_card),2)}\n'
            strg += f' Total Time Play :  {len(self.score_card)}\n'
            print(strg)
            # return strg
    # r=Tk()
    ##
    ##        r.title('Quiz Game Score Card ')
    # r.geometry('270x450+600+100')
    ##
    ##        l1=Label(r,text='SCORE CARD',font=(13),borderwidth=6,relief='groove')
    # l1.pack()
    # print(1)
    # l=Label(r,text=strg)
    # print(2)
    # l.pack()
    # b=Button(r,text='OK',font=(11),borderwidth=6,command=r.destroy)
    # b.pack()
    # r.mainloop()

            ##################################

            r = Tk()
            r.title('Quiz Game Score Card ')
            r.geometry('570x450+500+100')

            l1 = Label(r, text='SCORE CARD', font=(
                13), borderwidth=6, relief='groove')
            l1.pack()

            # Create a scrollbar
            scrollbar = Scrollbar(r)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Create a Text widget
            text = Text(r, yscrollcommand=scrollbar.set)

            # Insert the string variable 'strg' into the Text widget
            text.insert(INSERT, strg)

            text.pack(expand=True, fill='both')

            # Configure the scrollbar to work with the Text widget
            scrollbar.config(command=text.yview)

            b = Button(r, text='OK', font=(11),
                       borderwidth=6, command=r.destroy)
            b.pack()

            r.mainloop()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('error')
            msg.setText('you had not given any quiz till now !')
            # critical x imformation i Warning triangle question ?
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
