from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(N)]

# dp[y][x]: (0, 0)에서 (y, x)으로 이동하기 위해 부수어야 하는 벽의 최소 개수
dp = [[-1] * M for _ in range(N)]
dp[0][0] = 0

q = deque([(0, 0)])
while q:
    y, x = q.popleft()
    count = dp[y][x]
    
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_y, new_x = y + dy, x + dx
        if not (0 <= new_x < M and 0 <= new_y < N):
            continue

        # 뚫려 있을 때
        if grid[new_y][new_x] == 0:
            if 0 <= dp[new_y][new_x] <= count:
                continue
            dp[new_y][new_x] = count
        # 벽으로 막혀 있을 때
        else:
            if 0 <= dp[new_y][new_x] <= count + 1:
                continue
            dp[new_y][new_x] = count + 1
            
        q.append((new_y, new_x))

print(dp[N - 1][M - 1])