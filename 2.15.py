import math
x = float(input())
ep = float(input())
while not (0 < ep < 1):
    print("Nhap lai.")
    ep = float(input())
S = 0
n = 0
while True:
    term = (x**n) / math.factorial(n)
    if term < ep:
        break
    S += term
    n += 1
print(f"e^{x} = {S:.2f}")
