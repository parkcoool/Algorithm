import sys

input = sys.stdin.readline

*nums, _ = map(int, input().strip().split())
N = len(nums)

# dp[i][l][r]: i단계에서 왼쪽 발이 l, 오른쪽 발이 r에 있기 위한 최소 비용
dp = [[[float("inf")] * 5 for _ in range(5)] for _ in range(N + 1)]
dp[0][0][0] = 0

for index, num in enumerate(nums):
  index += 1

  # num: 한 쪽 발의 위치
  # opposite_num: 반대 발의 위치
  for opposite_num in range(5):
    if num == opposite_num: continue

    for i in range(5):
      cost = 0

      # 중앙에서 다른 지점으로
      if i == 0: cost = 2
      # 인접한 지점으로
      elif num == 0 or abs(i - num) % 2 == 1: cost = 3
      # 반대편으로
      elif abs(i - num) == 2: cost = 4
      # 같은 지점
      elif i == num: cost = 1
      
      dp[index][num][opposite_num] = min(
        dp[index][num][opposite_num],
        dp[index - 1][i][opposite_num] + cost
      )
      dp[index][opposite_num][num] = min(
        dp[index][opposite_num][num],
        dp[index - 1][opposite_num][i] + cost
      )

ans = float("inf")
for i in range(5):
  for j in range(5):
    ans = min(ans, dp[N][i][j])

print(ans)