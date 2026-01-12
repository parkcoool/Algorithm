from collections import Counter
from math import prod

def solution(clothes):
    counts = Counter([x[1] for x in clothes])
    return prod(map(lambda x: x+1, counts.values())) - 1
