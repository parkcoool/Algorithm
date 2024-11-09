from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

N = int(input())
A = list(map(int, input().split()))

# dp[i] = A[i] 부터 시작하는 부분 수열 길이의 최댓값
dp = [-1] * N
dp[N - 1] = 1

ans = 1
for i in range(N - 2, -1, -1):
  result = 1
  for j in range(i + 1, N):
    if A[j] > A[i]:
      result = max(result, dp[j] + 1)
  dp[i] = result
  ans = max(ans, result)

print(ans)