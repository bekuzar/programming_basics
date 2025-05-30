from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets
import sys
from main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_confirm.clicked.connect(self.save_user)
    
    def save_user(self):
        if self.validate():
            pass  # сохраняем в файл
        else:
            
    def validate(self):
        if self.ed_username.text.length == 0:
            return False
        if self.ed_password.text < 8:
            return False
        if self.ed_password.text != self.ed_confirm_pass.text:
            return False
        
        return True
    
    
    
        
    


app = QApplication(sys.argv)

win = MainWindow()

win.show()
app.exec()