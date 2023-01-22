from PyQt5 import QtCore, QtGui, QtWidgets                          ##Importing PyQt5 essentials
import sys
                     ##Importing class  Ui_createaccount from  file  createaccount
from PyQt5.QtWidgets import QMessageBox                       ##Importing file p_p_l.py
                                           ##Importing date and time
import datetime  
import pymysql
import USER


mydb=pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="", database="quiz game")
c=mydb.cursor()

class Ui_createaccount(object):
   
   def open_createaccount(self):                          ##method to create an instance of open account
       self.window=QtWidgets.QMainWindow()
       self.ui=Ui_createaccount()
       self.ui.setupUi(self.window)
       self.window.show()
       
   def open_USER(self):##method to create an instance of open account
       self.Dialog.hide()
       print(1)
       self.window=QtWidgets.QMainWindow()
       self.ui=USER.Ui_costomer()
       self.ui.setupUi(self.window)
       self.window.show()       
       
   def setupUi(self, Dialog):
       self.Dialog=Dialog
       ##Readymade setup class from Pyqt5
       Dialog.setObjectName("Dialog")
       Dialog.resize(379, 460)
       Dialog.setAutoFillBackground(False)
       self.widget = QtWidgets.QWidget(Dialog)
       self.widget.setGeometry(QtCore.QRect(0, 0, 371, 451))
       self.widget.setObjectName("widget")
       self.label = QtWidgets.QLabel(self.widget)
       self.label.setGeometry(QtCore.QRect(10, 10, 361, 441))
       self.label.setStyleSheet("\n""border-radius:20px;")
       self.label.setText("")
       self.label.setPixmap(QtGui.QPixmap("a2.jpg"))
       self.label.setScaledContents(True)
       self.label.setObjectName("label")
       self.label_2 = QtWidgets.QLabel(self.widget)
       self.label_2.setGeometry(QtCore.QRect(20, 90, 341, 31))
       font = QtGui.QFont()
       font.setPointSize(20)
       font.setBold(True)
       font.setWeight(75)
       self.label_2.setFont(font)
       self.label_2.setStyleSheet("    color:rgba(255,255,255,210);")
       self.label_2.setObjectName("label_2")
       self.lineEdit = QtWidgets.QLineEdit(self.widget)
       self.lineEdit.setGeometry(QtCore.QRect(80, 165, 200, 40))
       font = QtGui.QFont()
       font.setPointSize(10)
       font.setBold(False)
       font.setWeight(50)
       self.lineEdit.setFont(font)
       self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
       self.lineEdit.setText("")
       self.lineEdit.setObjectName("lineEdit")
       self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
       self.lineEdit_2.setGeometry(QtCore.QRect(80, 230, 200, 40))
       font = QtGui.QFont()
       font.setPointSize(10)
       font.setBold(False)
       font.setWeight(50)
       self.lineEdit_2.setFont(font)
       self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
       self.lineEdit_2.setText("")
       self.lineEdit_2.setObjectName("lineEdit_2")
       self.pushButton = QtWidgets.QPushButton(self.widget)
       self.pushButton.setGeometry(QtCore.QRect(60, 310, 131, 40))
       font = QtGui.QFont()
       font.setPointSize(12)
       font.setBold(True)
       font.setWeight(75)
       self.pushButton.setFont(font)
       self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
" background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0 stop:0 rgba(20,47,78,219) stop:1 rgba(85,98,112,226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
" background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0 stop:0 rgba(40,57,98,219) stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"padding-color:rgba(105,118,132,200);\n"
"}\n"
"\n"
"")
       self.pushButton.setObjectName("pushButton")
       self.label_3 = QtWidgets.QLabel(self.widget)
       self.label_3.setGeometry(QtCore.QRect(70, 370, 251, 20))
       font = QtGui.QFont()
       font.setPointSize(9)
       font.setBold(True)
       font.setWeight(75)
       self.label_3.setFont(font)
       self.label_3.setStyleSheet("color:rgba(255,255,255,40);")
       self.label_3.setObjectName("label_3")
       self.pushButton_2 = QtWidgets.QPushButton(self.widget)
       self.pushButton_2.setGeometry(QtCore.QRect(210, 310, 121, 40))
       font = QtGui.QFont()
       font.setPointSize(11)
       font.setBold(True)
       font.setWeight(75)
       self.pushButton_2.setFont(font)
       self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
" background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0 stop:0 rgba(20,47,78,219) stop:1 rgba(85,98,112,226));\n"
"  color:rgba(255,255,255,210);\n"
"  border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
" background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0 stop:0 rgba(40,57,98,219) stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"padding-color:rgba(105,118,132,200);\n"
"}\n"
"\n"
"")
       self.pushButton_2.setObjectName("pushButton_2")
       self.retranslateUi(Dialog)
       QtCore.QMetaObject.connectSlotsByName(Dialog)
       

       
##       self.pushButton.clicked.connect(Dialog.hide)
       


   def retranslateUi(self, Dialog):
       _translate = QtCore.QCoreApplication.translate
       Dialog.setWindowTitle(_translate("Dialog", "Create_Account"))
       self.label_2.setText(_translate("Dialog", "CREATE LOGIN ACCOUNT"))
       self.lineEdit.setPlaceholderText(_translate("Dialog", " USER NAME"))
       self.lineEdit_2.setPlaceholderText(_translate("Dialog", " PASSWORD"))
       self.pushButton.setText(_translate("Dialog", "Sign Up"))

       self.pushButton.clicked.connect(self.filing)
       
       self.label_3.setText(_translate("Dialog", "   Forgot Your User Name Or Password?"))
       self.pushButton_2.setText(_translate("Dialog", "Back"))
       self.pushButton_2.clicked.connect(self.open_USER)
   

##        Dialog.hide()
       
   def filing(self):           ##method to check if the user name and password exist in the file for not .Displays error if not in file.
       self.line1=self.lineEdit.text()
       self.line2=self.lineEdit_2.text()
    
       try:
           c.execute('select COUNT(user_name) from person where user_name=%s',(self.line1))
           exist=c.fetchall()
           exist=str(exist)
           exist=exist.strip("(").strip(")").strip(",").strip(")").strip(",").strip("'").strip("'")
           if exist =='':
              exist=0
           else:
              exist=exist
            
           
          
           exist=int(exist)
           

           if self.line1 =='' or self.line2 =='':
               msg=QMessageBox()
               msg.setWindowTitle('error')
               msg.setText("PLZ FILL ALL INPUTS !")
               msg.setIcon(QMessageBox.Critical) #critical x imformation i Warning triangle question ?
               x=msg.exec_()
              
      

           elif exist>0:
               msg=QMessageBox()
               msg.setWindowTitle('error')
               msg.setText("USER ALREDY EXIST !")
               msg.setIcon(QMessageBox.Critical) #critical x imformation i Warning triangle question ?
               x=msg.exec_()
           else:
              
              c.execute(''' insert into person (user_name,user_password) values(%s,%s) ''',(self.line1,self.line2))
             
              mydb.commit()
              print('your acc created')
              self.open_USER()
              
               
       except:
           
           print('error')
       


if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   Dialog = QtWidgets.QDialog()
   ui = Ui_createaccount()
   ui.setupUi(Dialog)
   Dialog.show()
   sys.exit(app.exec_())
