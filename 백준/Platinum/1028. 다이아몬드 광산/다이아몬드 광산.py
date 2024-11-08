row, col = map(int, input().split())
mine = [list(map(int, input())) for _ in range(row)]

right_diag = [[0] * col for _ in range(row)]
left_diag = [[0] * col for _ in range(row)]

for y in range(row - 1, -1, -1):
    for x in range(col - 1, -1, -1):
        if mine[y][x] == 0: continue

        left_diag[y][x] = left_diag[y + 1][
            x - 1] + 1 if y + 1 < row and x - 1 >= 0 else 1
        right_diag[y][x] = right_diag[y + 1][
            x + 1] + 1 if y + 1 < row and x + 1 < col else 1

ans = 0
for y in range(row):
    for x in range(col):
        size = min(left_diag[y][x], right_diag[y][x])
        if right_diag[y][x] < size: continue
        if left_diag[y][x] < size: continue
        while size > ans:
            if right_diag[y + size - 1][x - size + 1] < size:
                size -= 1
                continue
            if left_diag[y + size - 1][x + size - 1] < size:
                size -= 1
                continue
            ans = size
            break

print(ans)
