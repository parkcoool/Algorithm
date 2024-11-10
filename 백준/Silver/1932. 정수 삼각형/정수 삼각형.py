import sys

input = sys.stdin.readline

N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]

# dp[y][x] = (y, x)에서 시작했을 때 결과
dp = [[-1] * (y + 1) for y in range(N)]
dp[N - 1] = tri[N - 1]


def sol(y, x):
  if dp[y][x] != -1:
    return dp[y][x]

  result = tri[y][x] + max(sol(y + 1, x), sol(y + 1, x + 1))
  dp[y][x] = result
  return result


print(sol(0, 0))
