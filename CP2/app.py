import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from home import HomeWidget
from details.ui import DetailsWidget

class MainApplication(QMainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()
        self.setWindowTitle("Sổ Ghi Chú - Ứng Dụng Hoàn Chỉnh")
        self.setMinimumSize(1000, 700)
        self.setMaximumSize(1000, 700) # Khóa kích thước theo file thiết kế .ui của bạn
        
        # Sử dụng QStackedWidget làm bộ chuyển trang lớp nền
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        
        # Khởi tạo 2 trang giao diện
        self.home_page = HomeWidget()
        self.details_page = DetailsWidget()
        
        # Thêm các trang vào bộ quản lý trang (Stack)
        self.stacked_widget.addWidget(self.home_page)     # Trang chủ (Index 0)
        self.stacked_widget.addWidget(self.details_page)  # Trang chi tiết (Index 1)
        
        # KẾT NỐI SỰ KIỆN GIỮA CÁC TRANG (EVENT HANDLING)
        self.connect_app_events()

    def connect_app_events(self):
        # Sự kiện 1: Khi nhấn "Edit" ở trang chủ -> Gọi hàm thực hiện chuyển trang
        self.home_page.request_edit_page.connect(self.handle_go_to_details)
        
        # Sự kiện 2: Khi nhấn nút "Close" ở trang chi tiết -> Lưu nội dung thay đổi và quay lại trang chủ
        self.details_page.note_saved.connect(self.handle_save_and_return)
        
        # Sự kiện 3: Khi nhấn nút "X" hủy bỏ ở trang chi tiết -> Chuyển trang về lại trang chủ trực tiếp
        self.details_page.back_to_home.connect(self.handle_go_to_home)

    def handle_go_to_details(self, index, title, content):
        # Bỏ dữ liệu ghi chú hiện tại vào trang chi tiết để chỉnh sửa
        self.details_page.set_note_data(index, title, content)
        # Thực hiện CHUYỂN TRANG sang trang chi tiết (Index 1)
        self.stacked_widget.setCurrentIndex(1)

    def handle_save_and_return(self, index, new_title, new_content):
        # Gửi dữ liệu THAY ĐỔI NỘI DUNG về cho trang chủ lưu trữ và cập nhật lại UI
        self.home_page.update_note_content(index, new_title, new_content)
        # Thực hiện CHUYỂN TRANG quay về trang chủ (Index 0)
        self.stacked_widget.setCurrentIndex(0)

    def handle_go_to_home(self):
        # Thực hiện CHUYỂN TRANG quay về trang chủ trực tiếp
        self.stacked_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())