from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets
import sys
from main_window import Ui_MainWindow

import hashlib

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_confirm.clicked.connect(self.save_user)
    
    def save_user(self):
        if self.validate():
             user_type = None
             with open("db.txt", "w") as file:
                 if self.admin_radio.isChecked():
                     user_type = "Admin"
                 else:
                     user_type = "User"
                 hashed_pass = hashlib.sha256(self.ed_password.text().encode())
                 
                 file.write(self.ed_username.text() + " " + hashed_pass.hexdigest() + " " + user_type + "\n") # сохраняем в файл
        
            
    def validate(self):
        if len(self.ed_username.text()) == 0:
            return False
        if len(self.ed_password.text()) < 8:
            return False
        if self.ed_password.text() != self.ed_confirm_pass.text():
            return False
        if not self.admin_radio.isChecked() and not self.user_radio.isChecked():
            return False
        
        return True
    
    
    
        
    


app = QApplication(sys.argv)

win = MainWindow()

win.show()
app.exec()