m,n=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(m)]
total=sum(sum(row) for row in a)
tb=round(total/(m*n),2)
print(tb)
for i in range(m):
    for j in range(n):
        if a[i][j]>tb:
            print(a[i][j],i+1,j+1)