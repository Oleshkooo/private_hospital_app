# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appointment.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_B(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setStyleSheet("background-color: #F9DFF9;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(25, 0, 25, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit.setStyleSheet("font-size: 25px;\n"
"color: #3E3E3E;\n"
"border: none;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setStyleSheet("")
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2021, 11, 28), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_2.addWidget(self.dateEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_2.setStyleSheet("font-size: 25px;\n"
"color: #3E3E3E;\n"
"border: none;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setMaximumTime(QtCore.QTime(18, 0, 0))
        self.timeEdit.setMinimumTime(QtCore.QTime(9, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_2.addWidget(self.timeEdit)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_1.setStyleSheet("QPushButton {\n"
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
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_2.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Make an Appointment"))
        self.lineEdit.setText(_translate("MainWindow", "Choose the date"))
        self.lineEdit_2.setText(_translate("MainWindow", "Choose the time"))
        self.pushButton_1.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_B()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
