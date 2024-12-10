n = int(input())
if n < 1:
    print("Loi")
else:
    print(f"Cac so nguyen to trong khoang (1, {n}):")
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1): 
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")