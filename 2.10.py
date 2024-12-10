import math
x=float(input())
n=int(input())
s=0
for _ in range(n):
    s=math.sqrt(x+s)
s=1+s
print("s =",s)