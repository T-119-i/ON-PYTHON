n=int(input())
if n<=0:
    print("Loi")
else:
    kitu="0123456789ABCDEF"
    he16=""
    while n>0:
        he16=kitu[n%16]+he16
        n//=16
    print("So he 16:",he16)