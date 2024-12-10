n=int(input())
if n<=0:
    print("Loi")
else:
    bin=""
    while n>0:
        bin=str(n%2)+bin
        n//=2
    print("So nhi phan:",bin)