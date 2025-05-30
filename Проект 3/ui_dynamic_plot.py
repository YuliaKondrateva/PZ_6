from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font_label = QtGui.QFont()
        font_label.setPointSize(12)
        font_label.setBold(True)

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(100, 20, 400, 40))
        font_title = QtGui.QFont()
        font_title.setPointSize(16)
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setObjectName("label_title")

        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(100, 80, 180, 40))
        self.button_start.setFont(font_label)
        self.button_start.setObjectName("button_start")

        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(320, 80, 180, 40))
        self.button_stop.setFont(font_label)
        self.button_stop.setObjectName("button_stop")

        self.plot_widget = QtWidgets.QWidget(self.centralwidget)
        self.plot_widget.setGeometry(QtCore.QRect(50, 150, 500, 300))
        self.plot_widget.setObjectName("plot_widget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Динамическая линейная диаграмма"))
        self.label_title.setText(_translate("MainWindow", "Генерация графика в реальном времени"))
        self.button_start.setText(_translate("MainWindow", "Старт"))
        self.button_stop.setText(_translate("MainWindow", "Стоп"))
