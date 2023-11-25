from itertools import combinations

LINKS = {0: (1, 2, 3, 4), 1: (0, 2, 3, 5), 2: (0, 1, 4, 5), 3: (0, 1, 4, 5), 4: (0, 2, 3, 5), 5: (1, 2, 3, 4)}

N = int(input())
DICE = list(map(int, input().split()))

if N == 1:
    print(sum(DICE) - max(DICE))

else:
    MIN_SURFACE = min(DICE)

    MIN_EDGE = float("inf")
    for num in range(6):
        for surface in LINKS[num]:
            edge = DICE[num] + DICE[surface]
            if edge < MIN_EDGE:
                MIN_EDGE = edge

    MIN_CORNER = float("inf")
    for nums in combinations(range(6), 3):
        if not (
            nums[0] in LINKS[nums[1]]
            and nums[0] in LINKS[nums[2]]
            and nums[1] in LINKS[nums[0]]
            and nums[1] in LINKS[nums[2]]
            and nums[2] in LINKS[nums[0]]
            and nums[2] in LINKS[nums[1]]
        ):
            continue
        corner = DICE[nums[0]] + DICE[nums[1]] + DICE[nums[2]]
        if corner < MIN_CORNER:
            MIN_CORNER = corner

    answer = 0
    if N >= 3:
        answer = 4 * MIN_SURFACE * ((N - 2) ** 2 + N - 2) + MIN_SURFACE * ((N - 2) ** 2)
    answer += 4 * MIN_EDGE * (N - 1) + 4 * MIN_EDGE * (N - 2)
    answer += 4 * MIN_CORNER

    print(answer)