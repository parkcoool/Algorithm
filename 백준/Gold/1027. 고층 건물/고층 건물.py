from itertools import combinations
from fractions import Fraction

count = int(input())
buildings = list(map(int, input().split()))

counts = [0] * count
for comb in combinations(range(count), 2):
    n1 = min(comb)
    v1 = buildings[n1]
    n2 = max(comb)
    v2 = buildings[n2]

    visible = True
    for i in range(n1 + 1, n2):
        if Fraction((v2 - v1) * (i - n1), (n2 - n1)) + v1 <= buildings[i]:
            visible = False
    if visible:
        counts[n1] += 1
        counts[n2] += 1
        
print(max(counts))