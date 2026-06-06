
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class HomeWidget(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("home.ui", self)

        self.notes = [
            "Nội dung ghi chú 1",
            "Nội dung ghi chú 2",
            "Nội dung ghi chú 3"
        ]

    def edit_note(self, index):
        print(self.notes[index])

    def update_note(self, index, content):
        self.notes[index] = content