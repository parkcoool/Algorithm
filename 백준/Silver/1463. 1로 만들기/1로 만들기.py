N = int(input())

# dp[x]: 1에서 n으로 갈 때 필요한 최소 연산 횟수
dp = {1: 0}

for i in range(2, N + 1):
  if i % 3 == 0 and i % 2 == 0:
    dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1, dp[i - 1] + 1)
  elif i % 3 == 0:
    dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
  elif i % 2 == 0:
    dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
  else:
    dp[i] = dp[i - 1] + 1

print(dp[N])