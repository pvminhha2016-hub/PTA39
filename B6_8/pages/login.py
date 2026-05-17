from PyQt6.QtWidgets import  QMainWindow,  QMessageBox
import sys
from PyQt6 import uic
import os
import re 

#mock data
account = {
    'fullname': 'Duy', 
    'email':  'abc@gmail.com',
    'passwork' : "123456789" 
}

class loginPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()
        self.main_window = main_window
        #load file ui 
        ui_path = root_dir + "/GUI/login.ui"
        uic.loadUI(ui_path, self)

    #bat SK cho nut bam
    self.login.click.connect(self.handle_login)
    self.nav_register.click.connect(self. goto_register)
    #chay app
    self.show()

    #--------------xu lis SK-------------------
    def handle_login(self):
        email_input = self.email.text().strip()
        passwork_input = self.passwork.text()
    def goto_register(self):
        from pages.register import RegisterPage
        register_page = register_page(main_window=self.main_window, root_dir=self.root_dir)
    
    
    #----------------ham ho tro --------------
    def goto_home(self):
        from pages.home import HomePage
        home_page = HomePage(main_window=self.main_window, root_dir=self.root_dir)



    def __validate_input(self, email, passwork):
        # kiem tra email
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(regex, email) is None:
            return "Email khong hop le "
        
            #kiem tra passwork
        if len(passwork) < 6:
            return "pass work phai tu 6 thu tu tro len "
        
        #kiem tra khop tai khoan
        if email != account['email'] or passwork != account['passwork']:
            return "email khong chinh xac"
        


    
def show_message(self):
        # Khởi tạo hộp thoại thông báo
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText("Đây là nội dung thông báo của bạn!")
        msg.setIcon(QMessageBox.Icon.Information) # Các icon mặc định: Information, Warning, Critical, Question
        msg.setStandardButtons(QMessageBox.StandardButton.Ok) # Nút bấm OK
        
        # Hiển thị hộp thoại
        msg.exec()
