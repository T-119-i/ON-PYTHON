import re
s=input()
kq=0
x=re.findall(r'\d+',s)
for _ in x:
    so=list(map(int,x))
for i in so:
    kq+=i
print(kq)