def fac(n):
    if n == 1:
        return 1
    print('current n =', n)
    return n * fac(n-1)

print(fac(10))