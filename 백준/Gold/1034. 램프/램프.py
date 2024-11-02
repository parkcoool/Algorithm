from collections import Counter

N, M = map(int, input().split())
table = [list(map(int, input())) for _ in range(N)]
K = int(input())

patterns = ["".join(map(str, row)) for row in table]
pattern_counts = Counter(patterns)

answer = 0

for pattern, count in pattern_counts.items():
    zero_count = pattern.count('0')

    if zero_count <= K and zero_count % 2 == K % 2:
        answer = max(answer, count)

print(answer)
