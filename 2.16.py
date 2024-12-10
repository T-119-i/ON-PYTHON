import math
a,b,c=map(int,input().split())
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    cv=p*2
    dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("La tam giac")
    print("Chu vi: {0}, dien tich: {1}".format(cv,dt))
else:
    print("Khong tao thanh tam giac")