A = input()
B = input()

dp = [[0] * len(B) for _ in range(len(A))]

a, b = 0, 0
for i in range(len(A)):
  for j in range(len(B)):
    if B[j] == A[i]:
      dp[i][j] = 1
      if i > 0 and j > 0:
        dp[i][j] += dp[i - 1][j - 1]
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  
print(dp[len(A) - 1][len(B) - 1])