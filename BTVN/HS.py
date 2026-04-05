from quan_li_diem_so import QuanLyDiemHocSinh


hs1 = QuanLyDiemHocSinh("Nguyen Van A", "12A1", "THPT Nguyen Hue", 8, 7, 9)
hs2 = QuanLyDiemHocSinh("Nguyen Van B", "12A1", "THPT Nguyen Hue", 2, 5, 5)
hs3 = QuanLyDiemHocSinh("Nguyen Van C", "12A1", "THPT Nguyen Hue", 10, 9.5, 10)
hs4 = QuanLyDiemHocSinh("Nguyen Van D", "12A1", "THPT Nguyen Hue", 7, 10, 10)
hs5 = QuanLyDiemHocSinh("Nguyen Van E", "12A1", "THPT Nguyen Hue", 6, 4, 6)
hs6 = QuanLyDiemHocSinh("Nguyen Van F", "12A1", "THPT Nguyen Hue", 10, 5, 1)



diemTBMax = max(
    hs1.tinhDiemTrungBinh(),
    hs2.tinhDiemTrungBinh(),
    hs3.tinhDiemTrungBinh(),
    hs4.tinhDiemTrungBinh(),
    hs5.tinhDiemTrungBinh(),
    hs6.tinhDiemTrungBinh()
)


for hs in [hs1, hs2, hs3, hs4, hs5, hs6]:
    if (hs.tinhDiemTrungBinh() == diemTBMax):
        print(hs)











