import math

def solution(n):
    if n == 1: return 1
    if n == 2: return 2
    ans = 0
    for i in range(n // 2 + 1):
        if i * 2 > n: continue
        ans += math.comb(n - i, i)
    return ans % 1234567