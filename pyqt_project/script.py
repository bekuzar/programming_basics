from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets
import sys
from KhechPyside import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)

win = MainWindow()

win.show()
app.exec()