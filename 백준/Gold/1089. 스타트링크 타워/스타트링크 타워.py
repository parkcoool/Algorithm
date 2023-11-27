N = int(input())
SHAPES = {
    0: set([0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18]),
    1: set([2, 6, 10, 14, 18]),
    2: set([0, 1, 2, 6, 8, 9, 10, 12, 16, 17, 18]),
    3: set([0, 1, 2, 6, 8, 9, 10, 14, 16, 17, 18]),
    4: set([0, 2, 4, 6, 8, 9, 10, 14, 18]),
    5: set([0, 1, 2, 4, 8, 9, 10, 14, 16, 17, 18]),
    6: set([0, 1, 2, 4, 8, 9, 10, 12, 14, 16, 17, 18]),
    7: set([0, 1, 2, 6, 10, 14, 18]),
    8: set([0, 1, 2, 4, 6, 8, 9, 10, 12, 14, 16, 17, 18]),
    9: set([0, 1, 2, 4, 6, 8, 9, 10, 14, 16, 17, 18]),
}

SIGN_INPUT = []
for _ in range(5):
    SIGN_INPUT.append(input())

signs = []
for num in range(N):
    sign = []
    s = "\n".join([x[4 * num : 4 * num + 3] for x in SIGN_INPUT])
    for num in range(len(s)):
        if s[num] == "#":
            sign.append(num)
    signs.append(set(sign))

possible_nums = [set() for _ in range(N)]
for j in range(N):
    for num in range(10):
        if SHAPES[num] == SHAPES[num].union(signs[j]):
            possible_nums[j].add(num)

answer = 0
cnt = 1

for nums in possible_nums:
    cnt *= len(nums)

if cnt == 0:
    print(-1)
else:
    for i in range(N):
        m = int(cnt / len(possible_nums[i]))
        for num in possible_nums[i]:
            answer += m * num * 10 ** (N - i - 1)

    print(answer / cnt)
