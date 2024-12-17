m,n=map(int,input().split())
n2,p=map(int,input().split())
if n!=n2:
    print("So cot mtr a phai bang so dong mtr b")
    exit()
a=[list(map(int,input().split())) for _ in range(m)]
b=[list(map(int,input().split())) for _ in range(n)]
c=[[0]*p for _ in range(m)]
for i in range(m):
    for j in range(p):
        c[i][j]=sum(a[i][k]*b[k][j] for k in range(n))
for row in c:
    print(" ".join(map(str,row)))