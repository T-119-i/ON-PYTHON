import math
a = float(input())
while not (0 < a < 0.01):
    print("Nhap lai")
    a = float(input())
S = 0
n = 0

while True:
    term = 1 / math.factorial(2 * n + 1) 
    if term < a:
        break
    S += term
    n += 1
print(f"s = {S:.6f}")
