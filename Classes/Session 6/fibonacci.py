def fib(n):
    if n == 1:
        return 1
    print('current n =', n)
    return fib(n-1) * fib(n-2)

print(fib(10))
