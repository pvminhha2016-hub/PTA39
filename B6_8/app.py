from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic
import os

from pages.login import LoginPage  # trang dau tien truy cap
from pages.register import RegisterPage  # trang dau tien truy cap
from pages.home import HomePage  # trang dau tien truy cap

# lay duong dan den cac file con
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# chi chay khi run bang app.py
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #login_page = LoginPage(main_window=None, root_dir=BASE_DIR)
    #register_page = RegisterPage(main_window=None, root_dir=BASE_DIR)
    home_page = HomePage(main_window=None, root_dir=BASE_DIR, cur_acc={"fullname": "Diep Au", "email": "abc@gmail.com", "password": "123456"})
    sys.exit(app.exec())
