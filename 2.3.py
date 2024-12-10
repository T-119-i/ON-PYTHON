#(a#0)
import math
a=int(input())
while a==0:
    print("a khac 0")
    a=int(input())
b=int(input())
c=int(input())
delta=b*b - 4*a*c
if delta<0:
    print("VN")
elif delta==0:
    print("x =",-b/(2*a))
else:
    x1=(-b-math.sqrt(delta)) / (2*a)
    x2=(-b+math.sqrt(delta)) / (2*a)
    print(f"x1 = {x1:.2f} ,x2 = {x2:.2f}")