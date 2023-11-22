count = int(input())
cases = []
for i in range(count):
    x, y = input().split()
    cases.append(int(y) - int(x))

for dist in cases:
    n = 0

    while True:
        n += 1
        sum_seq = n // 2 * (1 + n // 2)
        if n % 2 == 1: sum_seq += (n + 1) // 2
        if sum_seq >= dist: break
    print(n)