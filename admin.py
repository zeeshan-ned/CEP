from PyQt5 import QtCore, QtGui, QtWidgets  # Importing PyQt5 essentials
import sys
# Importing class  Ui_createaccount from  file  createaccount

from PyQt5.QtWidgets import QMessageBox  # Importing file p_p_l.py
# Importing date and time
import start

from mode import Ui_Dialog
import webbrowser


class Ui_admin(object):

    def open_start(self):
        print(1)
        self.window = QtWidgets.QMainWindow()
        self.ui = start.Ui_Dialog()
        print(2)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):  # Readymade setup class from Pyqt5
        self.Dialog = Dialog
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
        self.label.setPixmap(QtGui.QPixmap("a1.jpg"))
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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Login"))
        self.label_2.setText(_translate("Dialog", "    ADMIN LOGIN AREA"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", " USER NAME"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", " PASSWORD"))
        self.pushButton.setText(_translate("Dialog", "L o g  I n"))

        self.label_3.setText(_translate(
            "Dialog", "   Forgot Your User Name Or Password?"))
        self.pushButton_2.setText(_translate("Dialog", "Back"))

        self.pushButton.clicked.connect(self.filing)
        self.pushButton_2.clicked.connect(self.back)

    def back(self):
        self.Dialog.hide()
        print('hi')
        self.open_start()

    # method to check if the user name and password exist in the file for not .Displays error if not in file.

    def filing(self):
        self.line1 = self.lineEdit.text()
        self.line2 = self.lineEdit_2.text()
        adminu = ['admin']
        adminp = ['admin']

        try:

            if self.line1 == '' or self.line2 == '':
                msg = QMessageBox()
                msg.setWindowTitle('error')
                msg.setText("PLZ FILL ALL INPUTS !")
                # critical x imformation i Warning triangle question ?
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()

            elif self.line1 in adminu and self.line2 in adminp and adminu.index(self.line1) == adminp.index(self.line2):

                try:
                    self.Dialog.hide()
                    print('welcome')
                    webbrowser.open("http://localhost/sherozz/admin.php")

                except:
                    msg = QMessageBox()
                    msg.setWindowTitle('error')
                    msg.setText(
                        "There is a bug that the login window in not hiding we are working on it thank you for your co-operation")
                    # critical x imformation i Warning triangle question ?
                    msg.setIcon(QMessageBox.Critical)
                    x = msg.exec_()

            else:

                msg = QMessageBox()
                msg.setWindowTitle('error')
                msg.setText("ERROR NO USER FOUND")
                # critical x imformation i Warning triangle question ?
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()

        except:
            print('error')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_admin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
