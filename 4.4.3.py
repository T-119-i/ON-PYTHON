class Sach:
    def __init__(self):
        self.ten=""
        self.trang=0
        self.gia=0
    def nhap(self):
        self.ten=input()
        self.trang=int(input())
        self.gia=int(input())
    def xuat(self):
        print("Ten sach: {0}, So trang: {1}, Gia tien: {2}".format(self.ten,self.trang,self.gia))
    def loc(self):
        return self.gia>100000 and self.trang<200
print("Nhap so luong sach: ")
n=int(input())
qsach=[]
for i in range(n):
    print("Nhap thong tin sach thu",i+1)
    sach=Sach()
    sach.nhap()
    qsach.append(sach)
for b in qsach:
    if b.loc():
        b.xuat()