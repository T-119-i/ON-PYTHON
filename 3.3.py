n = int(input())
tong_uoc = 0
for i in range(1, n):
    if n % i == 0:
        tong_uoc += i
if tong_uoc == n:
    print(f"{n} là số hoan hao")
else:
    print(f"{n} không phai la so hoan hao")
    
    
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
ket_qua = []
for x in range(a, b + 1):
    tong_uoc = 0
    for i in range(1, x + 1):
        if x % i == 0:
            tong_uoc += i
    if tong_uoc == 2 * x:
        ket_qua.append(x)
if len(ket_qua) > 0:
    print(f"Cac so hoan hao trong doan [{a}, {b}]:", ket_qua)
else:
    print(f"Khong co so hoan hao nao trong doan [{a}, {b}].")