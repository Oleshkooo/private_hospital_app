# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc16.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_16(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 800)
        MainWindow.setStyleSheet("background-color: #F9DFF9;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(120, 40, 260, 260))
        self.label_1.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_1.setText("")
        self.label_1.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_1.setObjectName("label_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(65, 365, 370, 50))
        self.lineEdit_1.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_1.setReadOnly(True)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 340, 101, 17))
        self.label_2.setStyleSheet("color:#7f8c8d")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 425, 101, 17))
        self.label_3.setStyleSheet("color:#7f8c8d")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(65, 450, 370, 50))
        self.lineEdit_2.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 515, 101, 17))
        self.label_4.setStyleSheet("color:#7f8c8d")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(65, 540, 370, 50))
        self.lineEdit_3.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 605, 101, 17))
        self.label_5.setStyleSheet("color:#7f8c8d")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(65, 630, 370, 50))
        self.lineEdit_4.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(234, 715, 201, 50))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"  padding: 15px 30px;\n"
"  font-size: 16px;\n"
"  border-radius: 15px;\n"
"  background: #2780DD;\n"
"  border: none;\n"
"  text-align: center;\n"
"  color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #2B5DAA;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(65, 715, 121, 50))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"  padding: 15px 30px;\n"
"  font-size: 16px;\n"
"  border-radius: 15px;\n"
"  background: #ED3C34;\n"
"  border: none;\n"
"  text-align: center;\n"
"  color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #AA2823;\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vanda Chester"))
        self.lineEdit_1.setText(_translate("MainWindow", "Vanda Chester"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Urologist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "20$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
