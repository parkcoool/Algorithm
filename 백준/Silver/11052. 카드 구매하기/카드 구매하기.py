import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

# dp[n]: 구매하려는 카드의 개수가 n개일 때 금액의 최댓값
dp = [0] + P[:]

for i in range(1, N + 1):
  for j in range(1, i):
    dp[i] = max(dp[i], dp[j] + P[i - j - 1])

print(dp[N])