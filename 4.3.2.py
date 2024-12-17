m,n=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(m)]
b=[list(map(int,input().split())) for _ in range(m)]
c=[[a[i][j] + b[i][j] for j in range(n)] for i in range(m)]
d=[[a[i][j] - b[i][j] for j in range(n)] for i in range(m)]
for row in c:
    print(" ".join(map(str,row)))
for row in d:
    print(" ".join(map(str,row)))