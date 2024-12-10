n = int(input())
s = 0
t = 1 
for i in range(1, 2*n + 2): 
    t *= i 
    if i % 2 == 1:
        s += t
print("s =", s)