class SinhVien:
    def __init__(self):
        pass
    def nhap(self):
        self.ten, self.ma, self.toan, self.triet, self.ltc = input().split()
        self.ma = int(self.ma)
        self.toan = float(self.toan)
        self.triet = float(self.triet)
        self.ltc = float(self.ltc)
        self.tb = (self.toan + self.triet + self.ltc) / 3
    def xuat(self):
        print(f"{self.ma} {self.ten} {self.toan:.2f} {self.triet:.2f} {self.ltc:.2f} {self.tb:.2f}")
    def hoc_lai(self):
        count = 0
        if self.toan < 4.0:
            count += 1
        if self.triet < 4.0:
            count += 1
        if self.ltc < 4.0:
            count += 1
        return count >= 2
n = int(input())
ds = []
for i in range(n):
    sv = SinhVien()
    sv.nhap()
    ds.append(sv)
print("Danh sach sinh vien hoc lai")
sv_hoc_lai = [sv for sv in ds if sv.hoc_lai()]
for sv in sv_hoc_lai:
    sv.xuat()
print(f"Danh sach nay co {len(sv_hoc_lai)} sinh vien phai hoc lai")