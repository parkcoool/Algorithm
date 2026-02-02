import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
reversed_heights = heights[::-1]

dp = [0] * N
max_scores = [0] * N

for i in range(1, N):
  dp[i] = max_scores[i - 1]

  required_height = heights[i] + B[i - 1]
  idx = bisect_left(reversed_heights, required_height)

  if idx < N:
    last_index = N - 1 - idx
    limit_index = min(last_index, i - 1)
            
    if limit_index >= 0:
      score_if_open = max_scores[limit_index] + A[i - 1]
      dp[i] = max(dp[i], score_if_open)

  max_scores[i] = max(max_scores[i - 1], dp[i])

print(dp[N - 1])