n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
tgiac_tren=True
for i in range(n):
    for j in range(i):
        if a[i][j]!=0:
            tgiac_tren=False
            break
    if not tgiac_tren:
        break
tgiac_duoi=True
for i in range(n):
    for j in range(i+1,n):
        if a[i][j] !=0:
            tgiac_duoi=False
            break
    if not tgiac_duoi:
        break
if tgiac_tren:
    print("UPPER TRIANGLE")
elif tgiac_duoi:
    print("LOWER TRIANGLE")
else:
    print("NONE")