def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        if a < n:
            yield a
        else:
            break


for i in fibonacci(1000000):
    print(i)
