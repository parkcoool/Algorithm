from math import sqrt


def is_pal(n):
    i = 0
    while 10**i <= n:
        i += 1
    for j in range(i // 2):
        if (n % (10 ** (j + 1))) // (10**j) != (n % (10 ** (i - j))) // (10 ** (i - j - 1)):
            return False
    return True


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
while True:
    if is_pal(n) and is_prime(n):
        print(n)
        break
    n += 1
