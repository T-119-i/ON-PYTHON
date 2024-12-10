import math
a,b,c=map(int,input().split())
if a==0:
    if b==0:
        if c==0:
            print("VSN")
        else:
            print("VN")
    else:
        print("x =",round(-b/c,2))
else:
    delta=b*b - 4*a*c
    if delta<0:
        print("VN")
    elif delta==0:
        print("x =",-b/(2*a))
    else:
        x1=(-b-math.sqrt(delta)) / (2*a)
        x2=(-b+math.sqrt(delta)) / (2*a)
        print(f"x1 = {x1:.2f} ,x2 = {x2:.2f}")