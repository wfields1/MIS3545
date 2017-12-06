# (25 points) Factoring of integers. 
# Write a program that asks the user for an integer and then prints out all its factors. 
# For example, when the user enters 150, the program should print 2 3 5 5

def factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for i in factor(150):
    print(i, end = " ")