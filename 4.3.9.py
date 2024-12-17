m, n = map(int, input().split()) 
a = [list(map(int, input().split())) for _ in range(m)] 
found = False
for i in range(m):
    tong_hang = sum(a[i]) 
    if tong_hang % 7 == 0:
        print(i + 2) 
        found = True
if not found:
    print("NO")