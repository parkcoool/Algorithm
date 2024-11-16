from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dp[0][0] = 1

q = deque([(0, 0)])
while q:
    y, x = q.popleft()

    if y == N - 1 and x == M - 1:
        print(dp[y][x])
        break

    for y_add, x_add in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        new_y, new_x = y + y_add, x + x_add
        if not (0 <= new_y < N and 0 <= new_x < M):
            continue
        if grid[new_y][new_x] == 0:
            continue
        if dp[new_y][new_x] != -1:
            continue
        dp[new_y][new_x] = dp[y][x] + 1
        q.append((new_y, new_x))