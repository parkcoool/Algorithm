import sys

INF = float("inf")
input = sys.stdin.readline

N = int(input())
costs = [tuple(map(int, input().split())) for _ in range(N)]

ans = INF

# 첫 번째 집의 색상 결정
for first_color in (0, 1, 2):
  dp = [[INF] * 3 for _ in range(N)]
  dp[0][first_color] = costs[0][first_color]
  
  for i in range(1, N):
    for c1 in range(3):
      for c2 in range(3):
        if c1 == c2: continue
        if i == N - 1 and c2 == first_color: continue
        dp[i][c2] = min(dp[i][c2], dp[i - 1][c1] + costs[i][c2])

  ans = min(ans, min(dp[N - 1]))

print(ans)