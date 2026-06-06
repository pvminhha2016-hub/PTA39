
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic
import os
import QStacked


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notes")
        self.resize(500, 300)

        self.notes = ["Ghi chú đầu tiên"]

        # Stack chứa các trang
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.create_home_page()
        self.create_detail_page()

        self.stack.setCurrentWidget(self.home_page)

    def create_home_page(self):
        self.home_page = QWidget()

        layout = QVBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.addItems(self.notes)

        btnOpen = QPushButton("Xem ghi chú")
        btnOpen.clicked.connect(self.open_note)

        layout.addWidget(self.listWidget)
        layout.addWidget(btnOpen)

        self.home_page.setLayout(layout)
        self.stack.addWidget(self.home_page)

    def create_detail_page(self):
        self.detail_page = QWidget()

        layout = QVBoxLayout()

        self.textEdit = QTextEdit()

        btnSave = QPushButton("Lưu")
        btnBack = QPushButton("Quay lại")

        btnSave.clicked.connect(self.save_note)
        btnBack.clicked.connect(self.go_home)

        layout.addWidget(self.textEdit)
        layout.addWidget(btnSave)
        layout.addWidget(btnBack)

        self.detail_page.setLayout(layout)
        self.stack.addWidget(self.detail_page)

    def open_note(self):
        row = self.listWidget.currentRow()

        if row >= 0:
            self.current_row = row
            self.textEdit.setText(self.notes[row])
            self.stack.setCurrentWidget(self.detail_page)

    def save_note(self):
        self.notes[self.current_row] = self.textEdit.toPlainText()

        self.listWidget.clear()
        self.listWidget.addItems(self.notes)

    def go_home(self):
        self.stack.setCurrentWidget(self.home_page)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())