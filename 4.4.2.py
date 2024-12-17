class Sach:
    def __init__(self):
        self.ten=""
        self.trang=0
        self.gia=0
    def nhap(self):
        self.ten=input()
        self.trang=int(input())
        self.gia=int(input())
        self.tb=round(self.trang/self.gia,2)
    def tb(self):
        return self.trang/self.gia
    def xuat(self):
        print("Ten sach: {0}, So trang: {1}, Gia tien: {2}, Gia trung binh/trang: {3}".format(self.ten,self.trang,self.gia,self.tb))
print("Nhap so luong sach: ")
n=int(input())
qsach=[]
for i in range(n):
    print("Nhap thong tin sach thu",i+1)
    sach=Sach()
    sach.nhap()
    qsach.append(sach)
qsach.sort(key=lambda x: (x.tb,x.ten))
for b in qsach:
    b.xuat()