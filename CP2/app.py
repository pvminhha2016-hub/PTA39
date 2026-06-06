from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6 import uic
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.home = uic.loadUi("home.ui")
        self.detail = uic.loadUi("detail.ui")

        self.stack.addWidget(self.home)
        self.stack.addWidget(self.detail)

        # 3 nút Edit
        self.home.pushButton.clicked.connect(
            lambda: self.open_note(self.home.label_2.text())
        )

        self.home.pushButton_2.clicked.connect(
            lambda: self.open_note(self.home.label_4.text())
        )

        self.home.pushButton_3.clicked.connect(
            lambda: self.open_note(self.home.label_6.text())
        )

        # nút Back ở trang 2
        self.detail.pushButton.clicked.connect(
            lambda: self.stack.setCurrentIndex(0)
        )

    def open_note(self, text):
        self.detail.textEdit.setText(text)
        self.stack.setCurrentIndex(1)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())