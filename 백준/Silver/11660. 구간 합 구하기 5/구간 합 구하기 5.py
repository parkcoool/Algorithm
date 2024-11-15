import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# D[y][x]: (1, 1) ~ (y, x)까지의 합
D = [[0] * (N + 1) for _ in range(N + 1)]
for y in range(1, N + 1):
    for x in range(1, N + 1):
        D[y][x] = D[y][x - 1] + grid[y - 1][x - 1]
for y in range(1, N + 1):
    for x in range(1, N + 1):
        D[y][x] += D[y - 1][x]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(D[y2][x2] - D[y1 - 1][x2] - D[y2][x1 - 1] + D[y1 - 1][x1 - 1])