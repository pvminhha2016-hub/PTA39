from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic
import os

from pages.login import LoginPage 
#trang dau tien truy cap

BASE_DIR = os.path.dirname(os.pardir.abspath(__file__))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # ke thua cac code init cua lop cha
        # dat ten cho app
        self.setWindowTitle("Application Pet App - login ")
        #load trang  login tu loginpages
        self.login_pages = LoginPage(main_window=self, root_dir=BASE_DIR)
        self.setCentralWidget
        self.show()


if __name__ == "__main":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())