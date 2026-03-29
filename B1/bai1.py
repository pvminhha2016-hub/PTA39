# oop : object
# tao lop vat nuoi
class Vat_nuoi(object):
    def __init__(self, giong=" ", mau_sac="",tuoi=0, cannag=0):
        self.__giong = giong
        self.__mau_sac = mau_sac
        self.__tuoi = tuoi
        self.__cannang = cannag

    def __str__(self) -> str:
        return f"Vatnuoi: {self.__giong}, {self.__mau_sac}, {self.__tuoi}, {self.__cannang}"
    

    def getGiong (self):
        return self.__giong
    def getMau_sac (self):
        return self.__mau_sac
    def getTuoi (self):
        return self.__tuoi
    def getCannang (self):
        return self.__cannang

    def  getGiong (self, giongmoi):
        if giongmoi == "": print(" gia tri ko dc de trong")
        else: self.__giong = giongmoi
    def  getMau_sac (self, mau_sacmoi):
        if mau_sacmoi == "": print(" gia tri ko dc de trong")
        else: self.__mau_sac = mau_sacmoi
    def  getTuoi (self, tuoimoi):
        if tuoimoi < 0 : print(" gia tri ko dc de trong")
        else: self.__tuoi = tuoimoi
    def  getCannang (self, cannangmoi):
        if cannangmoi < 0 : print(" gia tri ko dc de trong")
        else: self.__cannang = cannangmoi
# taodoi tuong
meo1 = Vat_nuoi("meo", "den")
print(meo1)

print(meo1.getTuoi())
meo1.setTuoi(tuoiMoi=2)

meo1.setcanang(cannangmoi=-1)
print(meo1.getCannang)
print(meo1)
