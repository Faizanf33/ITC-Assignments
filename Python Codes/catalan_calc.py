def fact(n):
    if (n == 0):
        return 1

    elif (n < 3):
        return n

    f = 1
    for i in range(n, 1, -1):
        f *= i

    return f

def catalan(n):
    return (fact(2 * n)) // (fact(n + 1) * fact(n))

for i in range(26):
    print(catalan(i))
