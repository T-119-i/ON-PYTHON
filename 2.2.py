a,b=map(float,input().split())
if a==0:
    if b<=0:
        print("Vo ly")
    else:
        print("Luon dung")
else:
    x=-b/a
    if x>0:
        print("x >",round(x,2))
    else:
        print("x <",round(x,2))