n, q = map(int, input().split())
s = input().strip()
for _ in range(q):
    l, r, c = input().split()
    l, r = int(l), int(r)
    dem = s[l-1:r].count(c)
    print(dem)