import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
points = list(map(int, input().split()))

ans = 0
lo, hi = 0, N
while lo <= hi:
  h = (lo + hi) // 2
  
  last = 0
  dark = 0
  
  for point in points:
    dark += max(0, point - h - last)
    last = point + h
  dark += max(0, N - last)

  if dark > 0:
    lo = h + 1
  else:
    ans = h
    hi = h - 1

print(ans)