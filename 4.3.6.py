n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
dx=True
for i in range (n):
    for j in range(i+1,n):
        if a[i][j] != a[j][i]:
            dx=False
            break
    if not dx:
        break
if dx:
    print("YES")
else: print("NO")