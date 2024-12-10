n=int(input())
s=0
n=abs(n)
while n>0:
    s+=n%10
    n//=10
print("s =",s)