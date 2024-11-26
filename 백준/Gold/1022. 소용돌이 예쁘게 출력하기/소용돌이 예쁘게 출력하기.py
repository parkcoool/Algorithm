r1, c1, r2, c2 = map(int, input().split())

ans = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
biggest = 0
for y in range(r1, r2 + 1):
    for x in range(c1, c2 + 1):
        # 사각형 크기 계산
        border_size = max(abs(y), abs(x))
        side_length = 2 * (border_size + 1) - 1

        # 사각형의 첫 숫자 계산
        init_num = 1
        if border_size >= 1:
            init_num = 4 * (border_size - 1) * border_size + 2

        num = 0
        if y == 0 and x == 0:
            num = 1
        elif y == -(border_size):
            num = init_num + side_length - 2 + border_size - x
        elif y == border_size:
            num = init_num + side_length * 3 - 4 + border_size + x
        elif x == -(border_size):
            num = init_num + side_length * 2 - 3 + border_size + y
        elif x == border_size:
            num = init_num - 1 + border_size - y

        ans[y - r1][x - c1] = num
        biggest = max(biggest, num)

fill = len(str(biggest))
for row in ans:
    for num in row:
        print(str(num).rjust(fill), end=" ")
    print()