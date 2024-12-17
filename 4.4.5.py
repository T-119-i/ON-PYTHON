class NVien:
    def __init__(self):
        pass
    def nhap(self):
        self.ten, self.ma, self.hsl, self.phu_cap = input().split()
        self.ma = int(self.ma)
        self.hsl = float(self.hsl)
        self.phu_cap = int(self.phu_cap)
        self.luong = self.hsl * 2000000 + self.phu_cap
    def luong(self):
        return self.hsl * 2000000 + self.phu_cap
    def xuat(self):
        print(f"{self.ma} {self.ten} {self.hsl:.2f} {self.phu_cap} {self.luong:.2f}")
    
n = int(input())
ds = []
for i in range(n):
    nv = NVien()
    nv.nhap()
    ds.append(nv)
print(f"Danh sach nhan vien da sap xep: {n}")
ds.sort(reverse=True, key=lambda x: x.luong)
for b in ds:
    b.xuat()
