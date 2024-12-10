a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
d=a1*b2-a2*b1
dx=c1*b2-c2*c1
dy=a1*c2-a2*c1
if d!=0:
    x=dx/d
    y=dy/d
    print("x = {:.2f}, y = {:.2f}".format(x,y))
elif dx==0 and dy==0:
    print("VSN")
else: print("VN")