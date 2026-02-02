import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
  A, B = map(int, input().split())
  ans = 1
  k = 1
  
  while True:
      S = 2**k - 1
      if S > A + B: break
      
      min_x = max(0, S - B)
      max_x = min(A, S)
      
      if min_x <= max_x: ans += max_x - min_x + 1
      k += 1
      
  print(ans)