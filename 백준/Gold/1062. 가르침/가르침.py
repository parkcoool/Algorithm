from itertools import combinations

WORD_CNT, CHAR_CNT = map(int, input().split())

if CHAR_CNT < 5:
    print(0)
else:
    basic = set(["a", "n", "t", "i", "c"])
    extra = set()
    words = []

    for _ in range(WORD_CNT):
        charset = set((input()[4:])[:-3])
        extra.update(charset)
        words.append(charset)
    extra.difference_update(basic)

    max_cnt = 0
    for comb in combinations(extra, min(CHAR_CNT - 5, len(extra))):
        union = basic.union(comb)
        cnt = 0
        for charset in words:
            if charset.issubset(union):
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)
