import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
grid = [[0] * M] + [[0] + list(map(int, input().split())) for _ in range(N)]

sum_right = [[0] * (M + 1) for _ in range(N + 1)]
sum_down = [[0] * (M + 1) for _ in range(N + 1)]
for y in range(1, N + 1):
    for x in range(1, M + 1):
        sum_right[y][x] = sum_right[y][x - 1] + grid[y][x]
        sum_down[y][x] = sum_down[y - 1][x] + grid[y][x]

ans = 0
for y in range(K + 1, N - K + 1):
    for x in range(K + 1, M - K + 1):
        if sum_right[y][x + K] - sum_right[y][x - K - 1] < K * 2 + 1: continue
        if sum_down[y + K][x] - sum_down[y - K - 1][x] < K * 2 + 1: continue
        ans += 1

print(ans)