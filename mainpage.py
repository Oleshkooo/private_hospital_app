import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow
import sys

app = PyQt5.QtWidgets.QApplication(sys.argv)

MainWindow = PyQt5.QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

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
    a = ui.lineEdit_46.text()
    place = binary_Search(list_doctor, a)
    if a in list_doctor:
        ui.pushButton_4.setText(f'Doctor {a} ')
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
    if a in list_specification:
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
            ui.pushButton_24.setText('Lydia Jokumsen')
            ui.pushButton_25.setText('Cili Kipling')

    if a == 'Proctologist':
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

        ui.pushButton_4.setText('Brian Schneider')
        ui.pushButton_24.setText('')
        ui.pushButton_25.setText('')
    if a == 'Surgeon':
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
        ui.pushButton_24.setText('Xenagoras Chaves')
        ui.pushButton_25.setText('')
    if a == 'Ophthalmologist':
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
        ui.pushButton_24.setText('Widald Serra')
        ui.pushButton_25.setText('')

    if a == 'Physician':
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
        ui.pushButton_24.setText('Armann Fujimoto')
        ui.pushButton_25.setText('')
    if a == 'Urologist':
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
        ui.pushButton_24.setText('Jennifer Kazlow')
        ui.pushButton_25.setText('')

    if a == 'Cardiologist':
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
        ui.pushButton_24.setText('Barnabas Budai')
        ui.pushButton_25.setText('')

    if a == 'Endocrinologist':
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
        ui.pushButton_24.setText('')
        ui.pushButton_25.setText('')

    if a == 'Neurologist':
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
        ui.pushButton_24.setText('')
        ui.pushButton_25.setText('')
    if a == 'Oncologist':
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
        ui.pushButton_24.setText('')
        ui.pushButton_25.setText('')
    if a == 'Dentist':
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
        ui.pushButton_24.setText('Nausikaa MacAslan')
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

        ui.pushButton_4.setText('No such results')

# Функція пошуку


ui.pushButton_26.clicked.connect(search)

MainWindow.show()
sys.exit(app.exec_())
