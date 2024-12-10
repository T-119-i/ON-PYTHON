n = int(input())
if n <= 0:
    print("n > 0")
else:
    fib1, fib2 = 1, 1 
    print("Cac so Fibonacci tu F(1) den F(n):")
    if n == 1:
        print(fib1)
        tong = fib1
    else:
        print(fib1, fib2, end=" ")
        tong = fib1 + fib2
        for i in range(3, n + 1):
            fib_next = fib1 + fib2
            print(fib_next, end=" ")
            tong += fib_next
            fib1, fib2 = fib2, fib_next
    print(f"\nTong cac so Fibonacci tu F(1) den F({n}): {tong}")
