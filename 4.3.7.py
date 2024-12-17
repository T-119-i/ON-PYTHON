n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
dcc=sum(a[i][i] for i in range(n))
dcp=sum(a[i][n-i-1] for i in range(n))
print("Dg cheo chinh:",dcc)
print("Dg cheo phu:",dcp)