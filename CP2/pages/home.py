
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class HomeWidget(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("home.ui", self)

        self.notes = ["noi dung ghi chu1","noi dung ghi chu2","noi dung ghi chu3"]

    def xem(self, chi_so):
        print(self.notes[chi_so])

def sua(self, chi_so, noi_dung):
    self.notes[chi_so] = noi_dung