import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

q = deque([(0, 0, 0)])
# dp[y][x][z]: 말의 움직임을 z번 사용했을 때 (0, 0)에서 (y, x)까지의 최소 동작 수
dp = [[[-1] * (K + 1) for _ in range(W)] for __ in range(H)]
dp[0][0][0] = 0

while q:
    y, x, z = q.popleft()
    movement = dp[y][x][z]

    dxs = [1, -1, 0, 0, 2, 2, 1, 1, -2, -2, -1, -1]
    dys = [0, 0, 1, -1, 1, -1, 2, -2, 1, -1, 2, -2]

    for i in range(4 if z >= K else 12):
        new_y, new_x = y + dys[i], x + dxs[i]
        
        if not (0 <= new_y < H and 0 <= new_x < W): continue
        if grid[new_y][new_x] == 1: continue

        # 말의 움직임
        if i > 3:
            if -1 < dp[new_y][new_x][z + 1] <= movement + 1: continue
            dp[new_y][new_x][z + 1] = movement + 1
            q.append((new_y, new_x, z + 1))
        # 일반 움직임
        else:
            if -1 < dp[new_y][new_x][z] <= movement + 1: continue
            dp[new_y][new_x][z] = movement + 1
            q.append((new_y, new_x, z))

ans = -1
for z in range(K + 1):
    result = dp[H - 1][W - 1][z]
    if result != -1 and (ans == -1 or result < ans):
        ans = result

print(ans)