import os
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5 import uic

class DetailsWidget(QWidget):
    # Tạo tín hiệu gửi dữ liệu (index_thư_mục, tiêu_đề, nội_dung) về trang chủ khi nhấn Close
    note_saved = pyqtSignal(int, str, str)
    # Tín hiệu khi người dùng muốn quay lại trang chủ không lưu
    back_to_home = pyqtSignal()

    def __init__(self, parent=None):
        super(DetailsWidget, self).__init__(parent)
        
        # Tải file UI bố cục tự động của bạn
        ui_path = os.path.join(os.path.dirname(__file__), 'main_layout.ui')
        uic.loadUi(ui_path, self)
        
        self.current_note_index = -1 # Lưu vị trí ghi chú đang sửa (-1 nghĩa là tạo mới)
        
        self.setup_icons()
        self.connect_events()

    def setup_icons(self):
        # Định dạng nút phẳng trong suốt cho các nút tính năng
        icon_button_style = """
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 14px;
                padding: 6px;
            }
            QPushButton:hover { background-color: rgba(0, 0, 0, 0.08); }
            QPushButton:pressed { background-color: rgba(0, 0, 0, 0.15); }
        """
        # Ánh xạ các nút bấm với file ảnh icon tương ứng
        button_icons = {
            self.pushButton_4: "image_8d3521.png",       # Chuông
            self.pushButton_5: "icon_collaborator.png",  # Người cộng tác
            self.pushButton_6: "icon_palette.png",       # Bảng màu
            self.pushButton_7: "image_8d353d.png",       # Hình ảnh
            self.pushButton_8: "icon_archive.png"        # Lưu trữ
        }

        for button, icon_file in button_icons.items():
            if button is not None:
                button.setText("") 
                if os.path.exists(icon_file):
                    button.setIcon(QIcon(icon_file))
                button.setIconSize(QSize(20, 20))
                button.setStyleSheet(icon_button_style)

    def connect_events(self):
        # Xử lý sự kiện nút "close" (Lưu dữ liệu thay đổi và chuyển trang)
        self.pushButton.clicked.connect(self.save_and_close)
        # Xử lý sự kiện nút "X" trên góc phải (Quay về không lưu)
        self.pushButton_10.clicked.connect(self.back_to_home.emit)

    def set_note_data(self, index, title, content):
        """Đổ dữ liệu ghi chú cũ lên form để chỉnh sửa"""
        self.current_note_index = index
        self.label_7.setText(title)           # Thay đổi nội dung tiêu đề label_7
        self.textEdit.setPlainText(content)   # Thay đổi nội dung ô nhập textEdit

    def save_and_close(self):
        # Lấy nội dung văn bản mới sau khi người dùng đã thay đổi
        updated_title = self.label_7.text()
        updated_content = self.textEdit.toPlainText()
        
        # Phát tín hiệu gửi dữ liệu đã thay đổi đi
        self.note_saved.emit(self.current_note_index, updated_title, updated_content)