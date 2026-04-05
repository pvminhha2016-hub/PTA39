class QuanLyDiemHocSinh:
    # ham khoi tao (hoTen, lop, truong, diemToan, diemVan, diemAnh)
    def __init__(self, hoTen="", lop="", truong="", diemToan=0, diemVan=0, diemAnh=0):
        self.__hoTen = hoTen
        self.__lop = lop
        self.__truong = truong
        self.__diemToan = diemToan
        self.__diemVan = diemVan
        self.__diemAnh = diemAnh
    
    # ham in thong tin (k in diem)
    def __str__(self) -> str:
        return f"Hoc sinh: {self.__hoTen}, lop: {self.__lop}, truong: {self.__truong}, diem trung binh: {self.tinhDiemTrungBinh()}"
    
    
    # getter
    # getHoTen, getLop, getTruong, getDiemToan, getDiemVan, getDiemAnh
    def getHoTen(self):
        return self.__hoTen
    def getLop(self):
        return self.__lop
    def getTruong(self):
        return self.__truong
    def getDiemToan(self):
        return self.__diemToan
    def getDiemVan(self):
        return self.__diemVan
    def getDiemAnh(self):
        return self.__diemAnh
    
    # setter
    # setHoTen, setLop, setTruong, setDiemToan, setDiemVan, setDiemAnh
    def setHoTen(self, hoTenMoi):
        if hoTenMoi == "": print("Gia tri khong duoc de trong")
        else: self.__hoTen = hoTenMoi
    def setLop(self, lopMoi):
        if lopMoi == "": print("Gia tri khong duoc de trong")
        else: self.__lop = lopMoi
    def setTruong(self, truongMoi):
        if truongMoi == "": print("Gia tri khong duoc de trong")
        else: self.__truong = truongMoi
    def setDiemToan(self, diemToanMoi):
        if diemToanMoi < 0 or diemToanMoi > 10: print("Gia tri khong hop le")
        else: self.__diemToan = diemToanMoi
    def setDiemVan(self, diemVanMoi):
        if diemVanMoi < 0 or diemVanMoi > 10: print("Gia tri khong hop le")
        else: self.__diemVan = diemVanMoi
    def setDiemAnh(self, diemAnhMoi):
        if diemAnhMoi < 0 or diemAnhMoi > 10: print("Gia tri khong hop le")
        else: self.__diemAnh = diemAnhMoi
    
    # ham tinh diem trung binh
    def tinhDiemTrungBinh(self):
        tong = self.__diemToan + self.__diemVan + self.__diemAnh
        diemTrungBinh = tong / 3
        return round(diemTrungBinh, 2) # lam tron 2 chu so thap phan