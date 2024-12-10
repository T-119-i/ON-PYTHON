x=int(input())
n=int(input())
s=1
for i in range(1,n+1):
    s+=x**i
print("s =",s)