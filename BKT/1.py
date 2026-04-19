class HocSinh:
    def __init__(self, ten, dia_chi, chieu_cao, can_nang, hoc_luc):
        self.ten = ten
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc

    # Cập nhật địa chỉ
    def cap_nhat_dia_chi(self, dia_chi_moi):
        self.dia_chi = dia_chi_moi

    # Cập nhật chiều cao và cân nặng
    def cap_nhat_suc_khoe(self, chieu_cao_moi, can_nang_moi):
        self.chieu_cao = chieu_cao_moi
        self.can_nang = can_nang_moi

    # Xuất thông tin
    def hien_thi(self):
        print("ten", self.ten)
        print("dia chi", self.dia_chi)
        print("chieu cao", self.chieu_cao)
        print("can nang", self.can_nang)
        print("hoc luc", self.hoc_luc)
