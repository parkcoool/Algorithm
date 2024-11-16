import math

N = int(input())

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return True

dp = {x: [] for x in range(1, N + 1)}
dp[1] = [2, 3, 5, 7]
for n in range(2, N + 1):
    for start in dp[n - 1]:
        for last in range(10):
            num = start * 10 + last
            if is_prime(num):
                dp[n].append(num)

print("\n".join(map(str, dp[N])))