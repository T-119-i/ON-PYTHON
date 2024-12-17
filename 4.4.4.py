class NVien:
    def __init__(self):
        pass
    def nhap(self):
        self.ma,self.ten,self.hsl,self.pcap=input().split()
        self.ma=int(self.ma)
        self.hsl=float(self.hsl)
        self.pcap=int(self.pcap)
        self.luong=self.hsl*2000000+self.pcap
    def luong(self):
        return self.hsl*2000000+self.pcap
    def xuat(self):
        print(f"{self.ma} {self.ten} {self.hsl:.2f} {self.pcap} {self.luong:.0f}")

n=int(input())
nv=[]
for i in range(n):
    nvien=NVien()
    nvien.nhap()
    nv.append(nvien)
nvien_min=nv[0]
for nvien in nv:
    if nvien.luong<nvien_min.luong:
        nvien_min=nvien
print("Nhan vien co luong thap nhat")
nvien_min.xuat()