from math import comb

T = int(input())  

for _ in range(T):
  n = int(input())
  ans = 0
  for three in range(n // 3 + 1):
    for two in range((n - three * 3) // 2 + 1):
      ans += comb(three + two, three) * comb(n - three * 2 - two, three + two)
  print(ans)