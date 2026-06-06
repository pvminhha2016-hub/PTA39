from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("main.ui", self)

        self.widget.hide()  

        self.pushButton_2.clicked.connect(self.mo_ghichu)
        self.pushButton.clicked.connect(self.dong_ghichu)

    def mo_ghichu(self):
        self.textEdit.setPlainText("day la ghi chu")
        self.widget.show()  

    def dong_ghichu(self):
        print(self.textEdit.toPlainText())   
        self.widget.hide()  


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())