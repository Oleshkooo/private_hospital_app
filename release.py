# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        MainWindow.setMaximumSize(QtCore.QSize(1400, 800))
        MainWindow.setStyleSheet("background-color: #F9DFF9;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1400, 800))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1400, 800))
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setAccessibleDescription("")
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("background-color: #F9DFF9;")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(465, 120, 470, 80))
        self.label.setStyleSheet("font-size: 40px;\n"
"color: #222222;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(440, 200, 520, 35))
        self.label_2.setStyleSheet("font-size: 25px;\n"
"color: #3E3E3E;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 382, 492, 49))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"  padding: 15px 30px;\n"
"  font-size: 16px;\n"
"  border-radius: 15px;\n"
"  background: #FAFAFA;\n"
"  border: none;\n"
"  color: #000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #f7f2f2;\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab)
        self.pushButton_24.setGeometry(QtCore.QRect(370, 431, 492, 49))
        self.pushButton_24.setStyleSheet("QPushButton {\n"
"  padding: 15px 30px;\n"
"  font-size: 16px;\n"
"  border-radius: 15px;\n"
"  background: #FAFAFA;\n"
"  border: none;\n"
"  color: #000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #f7f2f2;\n"
"}")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab)
        self.pushButton_25.setGeometry(QtCore.QRect(370, 480, 492, 49))
        self.pushButton_25.setStyleSheet("QPushButton {\n"
"  padding: 15px 30px;\n"
"  font-size: 16px;\n"
"  border-radius: 15px;\n"
"  background: #FAFAFA;\n"
"  border: none;\n"
"  color: #000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #f7f2f2;\n"
"}")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_46.setGeometry(QtCore.QRect(370, 320, 492, 51))
        self.lineEdit_46.setToolTip("")
        self.lineEdit_46.setStatusTip("")
        self.lineEdit_46.setWhatsThis("")
        self.lineEdit_46.setAccessibleName("")
        self.lineEdit_46.setAccessibleDescription("")
        self.lineEdit_46.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_46.setInputMask("")
        self.lineEdit_46.setText("")
        self.lineEdit_46.setFrame(True)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.pushButton_26 = QtWidgets.QPushButton(self.tab)
        self.pushButton_26.setGeometry(QtCore.QRect(880, 320, 161, 49))
        self.pushButton_26.setStyleSheet("QPushButton {\n"
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
        self.pushButton_26.setObjectName("pushButton_26")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1380, 5540))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(50, 30, 50, 30)
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 11, 0, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_23.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_2.addWidget(self.lineEdit_23, 7, 2, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_32.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_2.addWidget(self.lineEdit_32, 12, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 9, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_17.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_2.addWidget(self.lineEdit_17, 4, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 6, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_15.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_2.addWidget(self.lineEdit_15, 3, 2, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_31.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_31.setReadOnly(True)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_2.addWidget(self.lineEdit_31, 11, 2, 1, 1)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_39.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_39.setReadOnly(True)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout_2.addWidget(self.lineEdit_39, 15, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 16, 0, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_25.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_2.addWidget(self.lineEdit_25, 8, 2, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_30.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_30.setReadOnly(True)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_2.addWidget(self.lineEdit_30, 11, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 17, 0, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_24.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_2.addWidget(self.lineEdit_24, 8, 1, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_34.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_34.setReadOnly(True)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_2.addWidget(self.lineEdit_34, 13, 2, 1, 1)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_38.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_38.setReadOnly(True)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout_2.addWidget(self.lineEdit_38, 15, 2, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_2.addWidget(self.lineEdit_13, 2, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 5, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 1, 1, 1, 1)
        self.lineEdit_45 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_45.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_45.setReadOnly(True)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.gridLayout_2.addWidget(self.lineEdit_45, 18, 1, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_33.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_33.setReadOnly(True)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_2.addWidget(self.lineEdit_33, 12, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 12, 0, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_22.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_2.addWidget(self.lineEdit_22, 7, 1, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_19.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_2.addWidget(self.lineEdit_19, 5, 2, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_14.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_2.addWidget(self.lineEdit_14, 3, 1, 1, 1)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_40.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_40.setReadOnly(True)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.gridLayout_2.addWidget(self.lineEdit_40, 16, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 15, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 10, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_18.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_2.addWidget(self.lineEdit_18, 5, 1, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_28.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_2.addWidget(self.lineEdit_28, 10, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_26.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_2.addWidget(self.lineEdit_26, 9, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 14, 0, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_36.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_36.setReadOnly(True)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout_2.addWidget(self.lineEdit_36, 14, 1, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_12.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 2, 1, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_35.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_35.setReadOnly(True)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_2.addWidget(self.lineEdit_35, 14, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 8, 0, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_21.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_2.addWidget(self.lineEdit_21, 6, 2, 1, 1)
        self.lineEdit_42 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_42.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_42.setReadOnly(True)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.gridLayout_2.addWidget(self.lineEdit_42, 17, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_16.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_2.addWidget(self.lineEdit_16, 4, 1, 1, 1)
        self.lineEdit_44 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_44.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_44.setReadOnly(True)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.gridLayout_2.addWidget(self.lineEdit_44, 18, 2, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_29.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_2.addWidget(self.lineEdit_29, 10, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_27.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_2.addWidget(self.lineEdit_27, 9, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 18, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEdit_43 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_43.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_43.setReadOnly(True)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.gridLayout_2.addWidget(self.lineEdit_43, 17, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 7, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 13, 0, 1, 1)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_37.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_37.setReadOnly(True)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout_2.addWidget(self.lineEdit_37, 13, 1, 1, 1)
        self.lineEdit_41 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_41.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_41.setReadOnly(True)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.gridLayout_2.addWidget(self.lineEdit_41, 16, 1, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_20.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_2.addWidget(self.lineEdit_20, 6, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 0, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
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
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 3, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
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
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 4, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
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
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 5, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
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
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 6, 3, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setStyleSheet("QPushButton {\n"
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
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 7, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setStyleSheet("QPushButton {\n"
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
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 8, 3, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setStyleSheet("QPushButton {\n"
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
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 9, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_15.setStyleSheet("QPushButton {\n"
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
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 10, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_16.setStyleSheet("QPushButton {\n"
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
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 11, 3, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_17.setStyleSheet("QPushButton {\n"
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
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 12, 3, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_18.setStyleSheet("QPushButton {\n"
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
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 13, 3, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_19.setStyleSheet("QPushButton {\n"
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
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_2.addWidget(self.pushButton_19, 14, 3, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_20.setStyleSheet("QPushButton {\n"
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
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_2.addWidget(self.pushButton_20, 15, 3, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_21.setStyleSheet("QPushButton {\n"
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
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_2.addWidget(self.pushButton_21, 16, 3, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_22.setStyleSheet("QPushButton {\n"
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
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_2.addWidget(self.pushButton_22, 17, 3, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_23.setStyleSheet("QPushButton {\n"
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
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_2.addWidget(self.pushButton_23, 18, 3, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 255, 255))
        self.label_3.setStyleSheet("border: 5px solid #f7f2f2")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("profile.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(360, 120, 971, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(392, 110, 101, 17))
        self.label_4.setStyleSheet("color:#7f8c8d")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(731, 110, 91, 17))
        self.label_5.setStyleSheet("color:#7f8c8d")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(1071, 110, 111, 17))
        self.label_6.setStyleSheet("color:#7f8c8d")
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(700, 250, 290, 51))
        self.lineEdit_5.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(731, 223, 171, 17))
        self.label_8.setStyleSheet("color:#7f8c8d")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(565, 380, 270, 35))
        self.label_9.setStyleSheet("font-size: 25px;\n"
"color: #3E3E3E;\n"
"\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(565, 25, 270, 35))
        self.label_10.setStyleSheet("font-size: 25px;\n"
"color: #3E3E3E;\n"
"\n"
"")
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(230, 450, 971, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(250)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_6.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_8.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"border: none;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(262, 440, 181, 17))
        self.label_11.setStyleSheet("color:#7f8c8d")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(872, 440, 211, 17))
        self.label_12.setStyleSheet("color:#7f8c8d")
        self.label_12.setObjectName("label_12")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(625, 620, 150, 49))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(360, 250, 290, 51))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("padding: 15px 30px;\n"
"font-size: 16px;\n"
"border-radius: 15px;\n"
"background: #FAFAFA;\n"
"color: #000")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(392, 223, 171, 17))
        self.label_13.setStyleSheet("color:#7f8c8d")
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Private Hospital App"))
        self.label.setText(_translate("MainWindow", "Search for doctors online"))
        self.label_2.setText(_translate("MainWindow", "Make an appointment without leaving home"))
        self.lineEdit_46.setPlaceholderText(_translate("MainWindow", "Enter the last name or specialty "))
        self.pushButton_26.setText(_translate("MainWindow", "Find"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main Page"))
        self.lineEdit_23.setText(_translate("MainWindow", "Neurologist"))
        self.lineEdit_32.setText(_translate("MainWindow", "Rut Langer"))
        self.lineEdit_7.setText(_translate("MainWindow", "Ales Ruff"))
        self.lineEdit_17.setText(_translate("MainWindow", "ENT-doctor"))
        self.lineEdit_15.setText(_translate("MainWindow", "ENT-doctor"))
        self.lineEdit_31.setText(_translate("MainWindow", "Dentist"))
        self.lineEdit_39.setText(_translate("MainWindow", "Vanda Chester"))
        self.lineEdit_25.setText(_translate("MainWindow", "Cardiologist"))
        self.lineEdit_30.setText(_translate("MainWindow", "Nausikaa MacAslan"))
        self.lineEdit_24.setText(_translate("MainWindow", "Kristian Trevis"))
        self.lineEdit_34.setText(_translate("MainWindow", "Endocrinologist"))
        self.lineEdit_38.setText(_translate("MainWindow", "Urologist"))
        self.lineEdit_13.setText(_translate("MainWindow", "Cardiologist"))
        self.lineEdit_10.setText(_translate("MainWindow", "Armann Fujimoto"))
        self.lineEdit_45.setText(_translate("MainWindow", "Xenagoras Chaves"))
        self.lineEdit_33.setText(_translate("MainWindow", "Proctologist"))
        self.lineEdit_22.setText(_translate("MainWindow", "Jennifer Kazlow"))
        self.lineEdit_19.setText(_translate("MainWindow", "Physician"))
        self.lineEdit_14.setText(_translate("MainWindow", "Brian Schneider"))
        self.lineEdit_40.setText(_translate("MainWindow", "Dentist"))
        self.lineEdit_18.setText(_translate("MainWindow", "Dimas Bergman"))
        self.lineEdit_28.setText(_translate("MainWindow", "Mathieu Nanni"))
        self.lineEdit_26.setText(_translate("MainWindow", "Lydia Jokumsen"))
        self.lineEdit_36.setText(_translate("MainWindow", "Scarlet Neil"))
        self.lineEdit_12.setText(_translate("MainWindow", "Barnabas Budai"))
        self.lineEdit_35.setText(_translate("MainWindow", "Ophthalmologist"))
        self.lineEdit_11.setText(_translate("MainWindow", "Physician"))
        self.lineEdit_21.setText(_translate("MainWindow", "Oncologist"))
        self.lineEdit_42.setText(_translate("MainWindow", "Ophthalmologist"))
        self.lineEdit_16.setText(_translate("MainWindow", "Cili Kipling"))
        self.lineEdit_44.setText(_translate("MainWindow", "Surgeon"))
        self.lineEdit_29.setText(_translate("MainWindow", "Surgeon"))
        self.lineEdit_27.setText(_translate("MainWindow", "ENT-doctor"))
        self.lineEdit_43.setText(_translate("MainWindow", "Widald Serra"))
        self.lineEdit_37.setText(_translate("MainWindow", "Sarit Ridge"))
        self.lineEdit_41.setText(_translate("MainWindow", "Vaughan Marinov"))
        self.lineEdit_20.setText(_translate("MainWindow", "Elo Carson"))
        self.lineEdit_9.setText(_translate("MainWindow", "Nutritionist"))
        self.pushButton_5.setText(_translate("MainWindow", "More Info"))
        self.pushButton_6.setText(_translate("MainWindow", "More Info"))
        self.pushButton_7.setText(_translate("MainWindow", "More Info"))
        self.pushButton_8.setText(_translate("MainWindow", "More Info"))
        self.pushButton_9.setText(_translate("MainWindow", "More Info"))
        self.pushButton_10.setText(_translate("MainWindow", "More Info"))
        self.pushButton_11.setText(_translate("MainWindow", "More Info"))
        self.pushButton_12.setText(_translate("MainWindow", "More Info"))
        self.pushButton_13.setText(_translate("MainWindow", "More Info"))
        self.pushButton_14.setText(_translate("MainWindow", "More Info"))
        self.pushButton_15.setText(_translate("MainWindow", "More Info"))
        self.pushButton_16.setText(_translate("MainWindow", "More Info"))
        self.pushButton_17.setText(_translate("MainWindow", "More Info"))
        self.pushButton_18.setText(_translate("MainWindow", "More Info"))
        self.pushButton_19.setText(_translate("MainWindow", "More Info"))
        self.pushButton_20.setText(_translate("MainWindow", "More Info"))
        self.pushButton_21.setText(_translate("MainWindow", "More Info"))
        self.pushButton_22.setText(_translate("MainWindow", "More Info"))
        self.pushButton_23.setText(_translate("MainWindow", "More Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Doctors"))
        self.lineEdit_2.setText(_translate("MainWindow", "First name"))
        self.lineEdit_3.setText(_translate("MainWindow", "Last name"))
        self.lineEdit_4.setText(_translate("MainWindow", "Middle name"))
        self.label_4.setText(_translate("MainWindow", "First name*"))
        self.label_5.setText(_translate("MainWindow", "Last name*"))
        self.label_6.setText(_translate("MainWindow", "Middle name*"))
        self.lineEdit_5.setText(_translate("MainWindow", "Date of birth"))
        self.label_8.setText(_translate("MainWindow", "Date of birth*"))
        self.label_9.setText(_translate("MainWindow", "Contact Information"))
        self.label_10.setText(_translate("MainWindow", "Personal Information"))
        self.lineEdit_6.setText(_translate("MainWindow", "Phone number"))
        self.lineEdit_8.setText(_translate("MainWindow", "Email"))
        self.label_11.setText(_translate("MainWindow", "Phone number*"))
        self.label_12.setText(_translate("MainWindow", "Email*"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.label_13.setText(_translate("MainWindow", "Sex*"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "My Profile"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_1(object):
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ales Ruff"))
        self.lineEdit_1.setText(_translate("MainWindow", "Ales Ruff"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Nutritionist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "26$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_2(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Armann Fujimoto"))
        self.lineEdit_1.setText(_translate("MainWindow", "Armann Fujimoto"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Physician"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "30$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_3(object):
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
        self.pushButton_2.setGeometry(QtCore.QRect(234, 716, 201, 50))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Barnabas Budai"))
        self.lineEdit_1.setText(_translate("MainWindow", "Barnabas Budai"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Cardiologist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "24$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_4(object):
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
        self.pushButton_2.setGeometry(QtCore.QRect(243, 715, 201, 50))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Brian Schneider"))
        self.lineEdit_1.setText(_translate("MainWindow", "Brian Schneider"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "ENT-doctor"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "12$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc5.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_5(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Cili Kipling"))
        self.lineEdit_1.setText(_translate("MainWindow", "Cili Kipling"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "ENT-doctor"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "25$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc6.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_6(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Dimas Bergman"))
        self.lineEdit_1.setText(_translate("MainWindow", "Dimas Bergman"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Physician"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "25$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc7.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_7(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Elo Carson"))
        self.lineEdit_1.setText(_translate("MainWindow", "Elo Carson"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Oncologist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "35$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc8.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_8(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Jennifer Kazlow"))
        self.lineEdit_1.setText(_translate("MainWindow", "Jennifer Kazlow"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Neurologist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "21$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc9.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_9(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Kristian Trevis"))
        self.lineEdit_1.setText(_translate("MainWindow", "Kristian Trevis"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Cardiologist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "22$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc10.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_10(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Lydia Jokumsen"))
        self.lineEdit_1.setText(_translate("MainWindow", "Lydia Jokumsen"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "ENT-doctor"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "20$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc11.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_11(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Mathieu Nanni"))
        self.lineEdit_1.setText(_translate("MainWindow", "Mathieu Nanni"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Surgeon"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "30$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc12.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_12(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Nausikaa MacAslan"))
        self.lineEdit_1.setText(_translate("MainWindow", "Nausikaa MacAslan"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Dentist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "27$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc13.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_13(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Rut Langer"))
        self.lineEdit_1.setText(_translate("MainWindow", "Rut Langer"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Proctologist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "18$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc14.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_14(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Sarit Ridge"))
        self.lineEdit_1.setText(_translate("MainWindow", "Sarit Ridge"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Endocrinologist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "17$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc15.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_15(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Scarlet Neil"))
        self.lineEdit_1.setText(_translate("MainWindow", "Scarlet Neil"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Ophthalmologist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "17$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

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


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc17.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_17(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Vaughan Marinov"))
        self.lineEdit_1.setText(_translate("MainWindow", "Vaughan Marinov"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Dentist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "20$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc18.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_18(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Widald Serra"))
        self.lineEdit_1.setText(_translate("MainWindow", "Widald Serra"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Ophthalmologist"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "15$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doc19.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_19(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Xenagoras Chaves"))
        self.lineEdit_1.setText(_translate("MainWindow", "Xenagoras Chaves"))
        self.label_2.setText(_translate("MainWindow", "Full name"))
        self.label_3.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_2.setText(_translate("MainWindow", "Surgeon"))
        self.label_4.setText(_translate("MainWindow", "Working hours"))
        self.lineEdit_3.setText(_translate("MainWindow", "9.00 - 18.00"))
        self.label_5.setText(_translate("MainWindow", "$/hour"))
        self.lineEdit_4.setText(_translate("MainWindow", "24$"))
        self.pushButton_2.setText(_translate("MainWindow", "Make appointment"))
        self.pushButton_1.setText(_translate("MainWindow", "Close"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

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


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())


import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

MainW1 = QtWidgets.QMainWindow()
ui1 = Ui_MainWindow_1()
ui1.setupUi(MainW1)

MainW2 = QtWidgets.QMainWindow()
ui2 = Ui_MainWindow_2()
ui2.setupUi(MainW2)

MainW3 = QtWidgets.QMainWindow()
ui3 = Ui_MainWindow_3()
ui3.setupUi(MainW3)

MainW4 = QtWidgets.QMainWindow()
ui4 = Ui_MainWindow_4()
ui4.setupUi(MainW4)

MainW5 = QtWidgets.QMainWindow()
ui5 = Ui_MainWindow_5()
ui5.setupUi(MainW5)

MainW6 = QtWidgets.QMainWindow()
ui6 = Ui_MainWindow_6()
ui6.setupUi(MainW6)

MainW7 = QtWidgets.QMainWindow()
ui7 = Ui_MainWindow_7()
ui7.setupUi(MainW7)

MainW8 = QtWidgets.QMainWindow()
ui8 = Ui_MainWindow_8()
ui8.setupUi(MainW8)

MainW9 = QtWidgets.QMainWindow()
ui9 = Ui_MainWindow_9()
ui9.setupUi(MainW9)

MainW10 = QtWidgets.QMainWindow()
ui10 = Ui_MainWindow_10()
ui10.setupUi(MainW10)

MainW11 = QtWidgets.QMainWindow()
ui11 = Ui_MainWindow_11()
ui11.setupUi(MainW11)

MainW12 = QtWidgets.QMainWindow()
ui12 = Ui_MainWindow_12()
ui12.setupUi(MainW12)

MainW13 = QtWidgets.QMainWindow()
ui13 = Ui_MainWindow_13()
ui13.setupUi(MainW13)

MainW14 = QtWidgets.QMainWindow()
ui14 = Ui_MainWindow_14()
ui14.setupUi(MainW14)

MainW15 = QtWidgets.QMainWindow()
ui15 = Ui_MainWindow_15()
ui15.setupUi(MainW15)

MainW16 = QtWidgets.QMainWindow()
ui16 = Ui_MainWindow_16()
ui16.setupUi(MainW16)

MainW17 = QtWidgets.QMainWindow()
ui17 = Ui_MainWindow_17()
ui17.setupUi(MainW17)

MainW18 = QtWidgets.QMainWindow()
ui18 = Ui_MainWindow_18()
ui18.setupUi(MainW18)

MainW19 = QtWidgets.QMainWindow()
ui19 = Ui_MainWindow_19()
ui19.setupUi(MainW19)

MainWBook = QtWidgets.QMainWindow()
uiB = Ui_MainWindow_B()
uiB.setupUi(MainWBook)


class Customer:
    firstName = ''
    lastName = ''
    middleName = ''
    birthdayDate = ''
    phoneNumber = ''
    email = ''
    sex = ''

    def updateTxt():
        data = open("customers.txt", "w")
        data.write(Customer.firstName+"\n")
        data.write(Customer.lastName+"\n")
        data.write(Customer.middleName+"\n")
        data.write(Customer.birthdayDate+"\n")
        data.write(Customer.phoneNumber+"\n")
        data.write(Customer.email+"\n")
        data.write(Customer.sex+"\n")
        data.close()
        pass


def Save():
    Customer.lastName = ui.lineEdit_3.text()
    Customer.firstName = ui.lineEdit_2.text()
    Customer.middleName = ui.lineEdit_4.text()
    Customer.birthdayDate = ui.lineEdit_5.text()
    Customer.phoneNumber = ui.lineEdit_6.text()
    Customer.email = ui.lineEdit_8.text()
    Customer.sex = ui.comboBox.currentText()
    Customer.updateTxt()


def checkIfDefault():
    if ui.lineEdit_2.text() == "First name" or ui.lineEdit_3.text() == "Last name" or ui.lineEdit_4.text() == "Middle name" or ui.lineEdit_5.text() == "Date of birth" or ui.lineEdit_6.text() == "Phone number" or ui.lineEdit_8.text() == "Email":
        return 1
    else:
        return 0


def botBook():
    #id = 780892851
    if checkIfDefault() == 1:
        closeAll()
        return
    global date, time, fullName
    fullName = f"{Customer.lastName} {Customer.middleName} {Customer.firstName}"
    date = uiB.dateEdit.date().toString("dd.MM.yyyy")
    time = uiB.timeEdit.time().toString("hh:mm")
    closeAll()
    
    toWrite = f"*Name:* {fullName},\n*Date:* {date}, *Time:* {time}\n"

    file = open("apoInfo.txt", "a")
    file.write(toWrite)
    file.close()


def closeAll():
    MainWBook.close()
    close1()
    close2()
    close3()
    close4()
    close5()
    close6()
    close7()
    close8()
    close9()
    close10()
    close11()
    close12()
    close13()
    close14()
    close15()
    close16()
    close17()
    close18()
    close19()


def book():
    MainWBook.show()
    


def closeB():
    MainWBook.close()


def open1():
    MainW1.show()
    


def close1():
    MainW1.close()


def open2():
    MainW2.show()
    


def close2():
    MainW2.close()


def open3():
    MainW3.show()
    


def close3():
    MainW3.close()


def open4():
    MainW4.show()
    


def close4():
    MainW4.close()


def open5():
    MainW5.show()
    


def close5():
    MainW5.close()


def open6():
    MainW6.show()
    


def close6():
    MainW6.close()


def open7():
    MainW7.show()
    


def close7():
    MainW7.close()


def open8():
    MainW8.show()
    


def close8():
    MainW8.close()


def open9():
    MainW9.show()
    


def close9():
    MainW9.close()


def open10():
    MainW10.show()
    


def close10():
    MainW10.close()


def open11():
    MainW11.show()
    


def close11():
    MainW11.close()


def open12():
    MainW12.show()
    


def close12():
    MainW12.close()


def open13():
    MainW13.show()
    


def close13():
    MainW13.close()


def open14():
    MainW14.show()
    


def close14():
    MainW14.close()


def open15():
    MainW15.show()
    


def close15():
    MainW15.close()


def open16():
    MainW16.show()
    


def close16():
    MainW16.close()


def open17():
    MainW17.show()
    


def close17():
    MainW17.close()


def open18():
    MainW18.show()
    


def close18():
    MainW18.close()


def open19():
    MainW19.show()
    


def close19():
    MainW19.close()


def binary_Search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

dict_doctor = {'Ales Ruff' : open1, 'Armann Fujimoto' : open2, 'Barnabas Budai' : open3, 'Brian Schneider' : open4, 'Cili Kipling' : open5, 'Dimas Bergman' : open6,
               'Elo Carson' : open7, 'Jennifer Kazlow' : open8, 'Kristian Trevis' : open9, 'Lydia Jokumsen' : open10, 'Mathieu Nanni' : open11,
               'Nausikaa MacAslan' : open12,
               'Rut Langer' : open13, 'Sarit Ridge' : open14, 'Scarlet Neil' : open15, 'Vanda Chester' : open16, 'Vaughan Marinov' : open17, 'Widald Serra' : open18,
               'Xenagoras Chaves' : open19}

list_doctor = ['Ales Ruff', 'Armann Fujimoto', 'Barnabas Budai', 'Brian Schneider', 'Cili Kipling', 'Dimas Bergman',
               'Elo Carson', 'Jennifer Kazlow', 'Kristian Trevis', 'Lydia Jokumsen', 'Mathieu Nanni',
               'Nausikaa MacAslan',
               'Rut Langer', 'Sarit Ridge', 'Scarlet Neil', 'Vanda Chester', 'Vaughan Marinov', 'Widald Serra',
               'Xenagoras Chaves']

list_specification = ['ENT-doctor', 'Proctologist', 'Surgeon', 'Ophthalmologist', 'Physician',
                      'Urologist', 'Cardiologist', 'Endocrinologist', 'Neurologist',
                      'Oncologist', 'Dentist']

ui.pushButton_4.setStyleSheet("QPushButton {\n"
                              "  padding: 15px 30px;\n"
                              "  font-size: 16px;\n"
                              "  border-radius: 15px;\n"
                              "  background-color: #F9DFF9;\n"
                              "  border: none;\n"
                              "  color: #000;\n"

                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "  background: #f7f2f2;\n"
                              "}")
ui.pushButton_24.setStyleSheet("QPushButton {\n"
                               "  padding: 15px 30px;\n"
                               "  font-size: 16px;\n"
                               "  border-radius: 15px;\n"
                               "  background-color: #F9DFF9;\n"
                               "  border: none;\n"
                               "  color: #000;\n"

                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "  background: #f7f2f2;\n"
                               "}")
ui.pushButton_25.setStyleSheet("QPushButton {\n"
                               "  padding: 15px 30px;\n"
                               "  font-size: 16px;\n"
                               "  border-radius: 15px;\n"
                               "  background-color: #F9DFF9;\n"
                               "  border: none;\n"
                               "  color: #000;\n"

                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "  background: #f7f2f2;\n"
                               "}")


def search():
    try:
        ui.pushButton_4.disconnect()
        ui.pushButton_24.disconnect()
        ui.pushButton_25.disconnect()
    except:
        a = 0
    a = ui.lineEdit_46.text()
    place = binary_Search(list_doctor, a)
    if a in dict_doctor:
        ui.pushButton_4.setText(f'Doctor {a} ')
        ui.pushButton_24.setText('')
        ui.pushButton_25.setText('')
        ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                      "  padding: 15px 30px;\n"
                                      "  font-size: 16px;\n"
                                      "  border-radius: 15px;\n"
                                      "  background-color: #FFA;\n"
                                      "  border: none;\n"
                                      "  color: #000;\n"

                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "  background: #f7f2f2;\n"
                                      "}")
        ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")
        ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")
        ui.pushButton_4.clicked.connect(dict_doctor[a])
        
    elif a in list_specification:
        if a == 'ENT-doctor':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")
            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FAFAFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")

            ui.pushButton_4.setText('Brian Schneider')
            ui.pushButton_4.clicked.connect(open4)
            ui.pushButton_24.setText('Lydia Jokumsen')
            ui.pushButton_24.clicked.connect(open10)
            ui.pushButton_25.setText('Cili Kipling')
            ui.pushButton_25.clicked.connect(open5)

        elif a == 'Proctologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")

            ui.pushButton_4.setText('Rut Langer')
            ui.pushButton_4.clicked.connect(open13)
            ui.pushButton_24.setText('')
            ui.pushButton_25.setText('')
        elif a == 'Surgeon':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")
            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FAFAFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")

            ui.pushButton_4.setText('Mathieu Nanni')
            ui.pushButton_4.clicked.connect(open11)
            ui.pushButton_24.setText('Xenagoras Chaves')
            ui.pushButton_24.clicked.connect(open19)
            ui.pushButton_25.setText('')
        elif a == 'Ophthalmologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")
            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FAFAFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")

            ui.pushButton_4.setText('Scarlet Neil')
            ui.pushButton_4.clicked.connect(open15)
            ui.pushButton_24.setText('Widald Serra')
            ui.pushButton_24.clicked.connect(open18)
            ui.pushButton_25.setText('')

        elif a == 'Physician':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FAFAFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")

            ui.pushButton_4.setText('Dimas Bergman')
            ui.pushButton_4.clicked.connect(open6)
            ui.pushButton_24.setText('Armann Fujimoto')
            ui.pushButton_24.clicked.connect(open2)
            ui.pushButton_25.setText('')
        elif a == 'Urologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FAFAFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")

            ui.pushButton_4.setText('Vanda Chester')
            ui.pushButton_4.clicked.connect(open16)
            ui.pushButton_24.setText('')
            ui.pushButton_25.setText('')

        elif a == 'Cardiologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FAFAFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #f7f2f2;\n"
                                           "}")

            ui.pushButton_4.setText('Kristian Trevis')
            ui.pushButton_4.clicked.connect(open9)
            ui.pushButton_24.setText('Barnabas Budai')
            ui.pushButton_24.clicked.connect(open3)
            ui.pushButton_25.setText('')

        elif a == 'Endocrinologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")

            ui.pushButton_4.setText('Sarit Ridge')
            ui.pushButton_4.clicked.connect(open14)
            ui.pushButton_24.setText('')
            ui.pushButton_25.setText('')

        elif a == 'Neurologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")

            ui.pushButton_4.setText('Jennifer Kazlow')
            ui.pushButton_4.clicked.connect(open8)
            ui.pushButton_24.setText('')
            ui.pushButton_25.setText('')
        elif a == 'Oncologist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")

            ui.pushButton_4.setText('Elo Carson')
            ui.pushButton_4.clicked.connect(open7)
            ui.pushButton_24.setText('')
            ui.pushButton_25.setText('')
        elif a == 'Dentist':
            ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")

            ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #FAFAFA;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")
            ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #FFA;\n"
                                           "}")

            ui.pushButton_4.setText('Vaughan Marinov')
            ui.pushButton_4.clicked.connect(open17)
            ui.pushButton_24.setText('Nausikaa MacAslan')
            ui.pushButton_24.clicked.connect(open12)
            ui.pushButton_25.setText('')

    else:
        ui.pushButton_4.setStyleSheet("QPushButton {\n"
                                          "  padding: 15px 30px;\n"
                                          "  font-size: 16px;\n"
                                          "  border-radius: 15px;\n"
                                          "  background-color: #FFA;\n"
                                          "  border: none;\n"
                                          "  color: #000;\n"

                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "  background: #f7f2f2;\n"
                                          "}")

        ui.pushButton_24.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")
        ui.pushButton_25.setStyleSheet("QPushButton {\n"
                                           "  padding: 15px 30px;\n"
                                           "  font-size: 16px;\n"
                                           "  border-radius: 15px;\n"
                                           "  background-color: #F9DFF9;\n"
                                           "  border: none;\n"
                                           "  color: #000;\n"

                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "  background: #F9DFF9;\n"
                                           "}")

        ui.pushButton_24.setText('')
        ui.pushButton_25.setText('')
        ui.pushButton_4.setText('No such results')
        try:
            ui.pushButton_4.disconnect()
            ui.pushButton_24.disconnect()
            ui.pushButton_25.disconnect()
        except:
            a = 0

# Функція пошуку

try:
    data = open("customers.txt", "r")
    temp = data.read().splitlines()
    for i in range(len(temp)):
        Customer.firstName = temp[i]
        ui.lineEdit_2.setText(temp[i])
        i += 1
        Customer.lastName = temp[i]
        ui.lineEdit_3.setText(temp[i])
        i += 1
        Customer.middleName = temp[i]
        ui.lineEdit_4.setText(temp[i])
        i += 1
        Customer.birthdayDate = temp[i]
        ui.lineEdit_5.setText(temp[i])
        i += 1
        Customer.phoneNumber = temp[i]
        ui.lineEdit_6.setText(temp[i])
        i += 1
        Customer.email = temp[i]
        ui.lineEdit_8.setText(temp[i])
        i += 1
        Customer.sex = temp[i]
        ui.comboBox.setCurrentText(temp[i])
        if not data.readline():
            break

except:
    data = open("customers.txt", "w")




data.close()

ui.pushButton_3.clicked.connect(Save)

ui.pushButton_26.clicked.connect(search)

ui.pushButton_5.clicked.connect(open1)
ui.pushButton_6.clicked.connect(open2)
ui.pushButton_7.clicked.connect(open3)
ui.pushButton_8.clicked.connect(open4)
ui.pushButton_9.clicked.connect(open5)
ui.pushButton_10.clicked.connect(open6)
ui.pushButton_11.clicked.connect(open7)
ui.pushButton_12.clicked.connect(open8)
ui.pushButton_13.clicked.connect(open9)
ui.pushButton_14.clicked.connect(open10)
ui.pushButton_15.clicked.connect(open11)
ui.pushButton_16.clicked.connect(open12)
ui.pushButton_17.clicked.connect(open13)
ui.pushButton_18.clicked.connect(open14)
ui.pushButton_19.clicked.connect(open15)
ui.pushButton_20.clicked.connect(open16)
ui.pushButton_21.clicked.connect(open17)
ui.pushButton_22.clicked.connect(open18)
ui.pushButton_23.clicked.connect(open19)

uiB.pushButton_2.clicked.connect(closeB)
uiB.pushButton_1.clicked.connect(botBook)
ui1.pushButton_1.clicked.connect(close1)
ui1.pushButton_2.clicked.connect(book)
ui2.pushButton_1.clicked.connect(close2)
ui2.pushButton_2.clicked.connect(book)
ui3.pushButton_1.clicked.connect(close3)
ui3.pushButton_2.clicked.connect(book)
ui4.pushButton_1.clicked.connect(close4)
ui4.pushButton_2.clicked.connect(book)
ui5.pushButton_1.clicked.connect(close5)
ui5.pushButton_2.clicked.connect(book)
ui6.pushButton_1.clicked.connect(close6)
ui6.pushButton_2.clicked.connect(book)
ui7.pushButton_1.clicked.connect(close7)
ui7.pushButton_2.clicked.connect(book)
ui8.pushButton_1.clicked.connect(close8)
ui8.pushButton_2.clicked.connect(book)
ui9.pushButton_1.clicked.connect(close9)
ui9.pushButton_2.clicked.connect(book)
ui10.pushButton_1.clicked.connect(close10)
ui10.pushButton_2.clicked.connect(book)
ui11.pushButton_1.clicked.connect(close11)
ui11.pushButton_2.clicked.connect(book)
ui12.pushButton_1.clicked.connect(close12)
ui12.pushButton_2.clicked.connect(book)
ui13.pushButton_1.clicked.connect(close13)
ui13.pushButton_2.clicked.connect(book)
ui14.pushButton_1.clicked.connect(close14)
ui14.pushButton_2.clicked.connect(book)
ui15.pushButton_1.clicked.connect(close15)
ui15.pushButton_2.clicked.connect(book)
ui16.pushButton_1.clicked.connect(close16)
ui16.pushButton_2.clicked.connect(book)
ui17.pushButton_1.clicked.connect(close17)
ui17.pushButton_2.clicked.connect(book)
ui18.pushButton_1.clicked.connect(close18)
ui18.pushButton_2.clicked.connect(book)
ui19.pushButton_1.clicked.connect(close19)
ui19.pushButton_2.clicked.connect(book)

# виходим з вікна
sys.exit(app.exec_())
