T = int(input())
N = []

for _ in range(T):
    N.append(int(input()))

dp = {0: (1, 0), 1: (0, 1)}

for n in N:
    for i in range(2, n + 1):
        dp[i] = (dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1])
    print(*dp[n])
