from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os
import re

class HomePage(QMainWindow):
    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc
        # load file ui
        ui_path = self.root_dir + "/GUI/main.ui"
        uic.loadUi(ui_path, self)
        
        # chuyen ten thanh ten nguoi dung hien tai
        self.user_name.setText(self.cur_acc["fullname"])
        
        # hien thi giao dien
        self.show()
    