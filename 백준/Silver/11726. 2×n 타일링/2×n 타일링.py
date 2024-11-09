from math import comb

n = int(input())

ans = 0
for garo in range(n // 2 + 1):
  ans += comb(n - garo, garo)

print(ans % 10007)