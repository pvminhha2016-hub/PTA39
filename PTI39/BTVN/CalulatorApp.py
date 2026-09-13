import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class CalulatorApp (QMainWindow):
    def __init__(self):
        super().__init__()
        #khai bbao bien input 
        self.input = " "
        #hien thi giao dien
        ui_path = os.path.join(os.path.dirname(__file__), "CalulatorApp.ui")  
        uic.loadUi(ui_path, self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalulatorApp()
    sys.exit(app.exec())
        



    self.khong.clicked.connect(self.bam_0)
    self.mot.clicked.connect(self.bam_1)
    self.hai.clicked.connect(self.bam_2)
    self.ba.clicked.connect(self.bam_3)
    self.bon.clicked.connect(self.bam_4)
    self.nam.clicked.connect(self.bam_5)
    self.sau.clicked.connect(self.bam_6)
    self.bay.clicked.connect(self.bam_7)
    self.tam.clicked.connect(self.bam_8)
    self.chin.clicked.connect(self.bam_9)
    self.cham.clicked.connect(self.bam_cham)

    
    self.cong.clicked.connect(self.bam_cong)
    self.tru.clicked.connect(self.bam_tru)
    self.nhan.clicked.connect(self.bam_nhan)
    self.chia.clicked.connect(self.bam_chia)

        
    self.pushButton_5.clicked.connect(self.Bang_tinh)

    def bam_0(self):
        self.add_text("0")

    def bam_1(self):
        self.add_text("1")

    def bam_2(self):
        self.add_text("2")

    def bam_3(self):
        self.add_text("3")

    def bam_4(self):
        self.add_text("4")

    def bam_5(self):
        self.add_text("5")

    def bam_6(self):
        self.add_text("6")

    def bam_7(self):
        self.add_text("7")

    def bam_8(self):
        self.add_text("8")

    def bam_9(self):
        self.add_text("9")

    def bam_cham(self):
        self.add_text(".")

    def bam_cong(self):
        self.add_text("+")

    def bam_tru(self):
        self.add_text("-")

    def bam_nhan(self):
        self.add_text("*")

    def bam_chia(self):
        self.add_text("/")

    def add_text(self, text):
        self.lineEdit.setText(self.lineEdit.text() + text)

    def Bang_tinh(self):
        try:
            result = str(eval(self.lineEdit.text()))
            self.lineEdit.setText(result)
        except:
            self.lineEdit.setText("Loi")


