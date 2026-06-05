from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFrame

class HomeWidget(QWidget):
    # Tín hiệu yêu cầu chuyển trang sang trang sửa ghi chú (gửi kèm vị trí, tiêu đề, nội dung)
    request_edit_page = pyqtSignal(int, str, str)

    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)
        
        # Khởi tạo dữ liệu danh sách 3 ghi chú mặc định ban đầu
        self.notes_data = [
            {"title": "Ghi chú 1", "content": "Nội dung ghi chú số 1..."},
            {"title": "Ghi chú 2", "content": "Nội dung ghi chú số 2..."},
            {"title": "Ghi chú 3", "content": "Nội dung ghi chú số 3..."}
        ]
        
        self.init_ui()

    def init_ui(self):
        # Bố cục chính theo chiều dọc
        main_layout = QVBoxLayout(self)
        
        title_label = QLabel("SỔ GHI CHÚ CỦA TÔI", self)
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #bb9744; margin-bottom: 15px;")
        main_layout.addWidget(title_label)
        
        # Bố cục hàng ngang chứa 3 cột ghi chú
        self.cards_layout = QHBoxLayout()
        main_layout.addLayout(self.cards_layout)
        
        # Vẽ danh sách ghi chú lên màn hình
        self.render_notes()

    def render_notes(self):
        """Hàm xóa giao diện cũ và vẽ lại giao diện mới mỗi khi dữ liệu thay đổi"""
        # Xóa các widget cũ trong layout (nếu có)
        while self.cards_layout.count():
            child = self.cards_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Tạo lại các thẻ ghi chú dựa trên dữ liệu cập nhật mới nhất
        for index, note in enumerate(self.notes_data):
            card = QFrame()
            card.setStyleSheet("background-color: #b49650; border-radius: 8px; padding: 10px;")
            card_layout = QVBoxLayout(card)
            
            lbl_title = QLabel(note["title"])
            lbl_title.setStyleSheet("font-weight: bold; font-size: 16px; color: white;")
            
            lbl_content = QLabel(note["content"])
            lbl_content.setWordWrap(True)
            lbl_content.setStyleSheet("color: #f5f5f5;")
            
            btn_edit = QPushButton("Edit")
            btn_edit.setStyleSheet("background-color: white; color: #b49650; font-weight: bold; border-radius: 4px; padding: 5px;")
            
            # Sử dụng tính năng "lambda" để bắt đúng vị trí index của nút được bấm
            btn_edit.clicked.connect(lambda checked, i=index: self.on_edit_clicked(i))
            
            card_layout.addWidget(lbl_title)
            card_layout.addWidget(lbl_content, 1) # Giãn cách nội dung
            card_layout.addWidget(btn_edit)
            
            self.cards_layout.addWidget(card)

    def on_edit_clicked(self, index):
        # Lấy dữ liệu hiện tại của ghi chú được chọn
        note = self.notes_data[index]
        # Bắn tín hiệu chuyển trang kèm theo dữ liệu
        self.request_edit_page.emit(index, note["title"], note["content"])

    def update_note_content(self, index, new_title, new_content):
        """Hàm nhận dữ liệu đã chỉnh sửa từ trang chi tiết gửi về và cập nhật vào mảng"""
        if 0 <= index < len(self.notes_data):
            self.notes_data[index]["title"] = new_title
            self.notes_data[index]["content"] = new_content
            self.render_notes() # Vẽ lại giao diện với nội dung mới!