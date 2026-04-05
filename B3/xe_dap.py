from lop_cha import Xe


class Xedap(Xe):
    def __init__(self, hang="", mauSac="", giaTien=0):
        super().__init__(hang, mauSac, giaTien)


    #over
    def run(self):
        hang = self._xe__hang
        
        return f"xe{hang} dang dc nhap"
    


xeDap = Xedap("hang 1 ", "xanh la + tim,10000")
print(Xe)
print(Xedap.khoiDong())
print(Xedap.run())