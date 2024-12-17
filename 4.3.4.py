m,n =map(int,input().split())
a=[]
for _ in range(m):
    a.append(list(map(int,input().split())))
b=[]
for _ in range(m):
    b.append(list(map(int,input().split())))
c=[]
for i in range(m):
    row=[a[i][j] + b[i][j] for j in range(n)]
    c.append(row)
for row in c:
    print(*row)