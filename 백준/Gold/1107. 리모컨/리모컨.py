N = int(input())
D = 10 - int(input())
digits = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if (D < 10):
    broken_digits = set(map(int, input().split()))
    digits -= broken_digits

ans = abs(N - 100)

if 0 in digits:
    ans = min(ans, 1 + N)

for num in range(1, 1000001):
    n = 0
    is_valid = True
    while 10**n <= num:
        n += 1
        digit = num % (10 ** n) // (10 ** (n - 1))
        if digit not in digits:
            is_valid = False
            break

    if not is_valid: continue
        
    result = abs(N - num) + n
    if result < ans:
        ans = result

print(ans)