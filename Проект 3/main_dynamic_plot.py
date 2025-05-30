import sys
import random
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ui_dynamic_plot import Ui_MainWindow

class DynamicPlotApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.canvas = FigureCanvas(Figure())
        self.ui.plot_widget.layout = QtWidgets.QVBoxLayout(self.ui.plot_widget)
        self.ui.plot_widget.layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111)

        self.x_data = []
        self.y_data = []
        self.counter = 0

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.add_point)

        self.ui.button_start.clicked.connect(self.start_plotting)
        self.ui.button_stop.clicked.connect(self.stop_plotting)

    def add_point(self):
        self.counter += 1
        self.x_data.append(self.counter)
        self.y_data.append(random.uniform(0, 10))

        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, color='blue', linewidth=2)
        self.ax.set_xlim(left=max(0, self.counter - 20), right=self.counter + 1)
        self.ax.set_ylim(0, 12)
        self.canvas.draw()

    def start_plotting(self):
        self.timer.start(1000)

    def stop_plotting(self):
        self.timer.stop()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = DynamicPlotApp()
    window.show()
    sys.exit(app.exec_())
