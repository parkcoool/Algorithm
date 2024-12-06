import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0] * (M + 1)] + [[0] + list(map(int, input().rstrip())) for _ in range(N)]

# S[y][x]: grid[0][0] ~ grid[y][x]의 합
S = [[0] * (M + 1) for _ in range(N + 1)]
for y in range(1, N + 1):
    for x in range(1, M + 1):
        S[y][x] = S[y - 1][x] + S[y][x - 1] - S[y - 1][x - 1] + grid[y][x]

def area(y1, x1, y2, x2):
    global S
    result = S[y2][x2] - S[y2][x1 - 1] - S[y1 - 1][x2] + S[y1 - 1][x1 - 1]
    return result

ans = 0
for y in range(2, N + 1):
    for x in range(2, M + 1):
        a = area(1, 1, y - 1, x - 1)
        b = area(1, x, y - 1, M)
        c = area(y, 1, N, x - 1)
        d = area(y, x, N, M)
        
        ans = max(ans, (a + b) * c * d)
        ans = max(ans, (a + c) * b * d)
        ans = max(ans, (c + d) * a * b)
        ans = max(ans, (b + d) * a * c)

for x1 in range(2, M):
    for x2 in range(x1 + 1, M + 1):
        a = area(1, 1, N, x1 - 1)
        b = area(1, x1, N, x2 - 1)
        c = area(1, x2, N, M)

        ans = max(ans, a * b * c)

for y1 in range(2, N):
    for y2 in range(y1 + 1, N + 1):
        a = area(1, 1, y1 - 1, M)
        b = area(y1, 1, y2 - 1, M)
        c = area(y2, 1, N, M)

        ans = max(ans, a * b * c)
        
print(ans)