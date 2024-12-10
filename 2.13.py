n = int(input())
S = 0 
gt = 1 

for k in range(n + 1):
    for i in range(1, 2 * k + 2):
        gt *= i
    term = 1 / gt
    S += term
    gt = 1

print(f"Tong S với n = {n} là: {S:.2f}")