n=int(input())
if n<0:
    print("Khong tinh duoc")
else:
    gt=1
    for i in range(1,n+1):
        gt*=i
    print(gt)