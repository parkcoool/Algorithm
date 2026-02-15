import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip().split()))

ans = [0, 0]
min_val = float("inf")
for a, a_val in enumerate(nums):
  if a == N - 1: continue
  
  b = min(bisect_left(nums, -a_val, lo=a + 1), N - 1)

  for b in (b - 1, b):
    if b < 0 or a == b: continue
      
    b_val = nums[b]
    val = abs(a_val + b_val)
    
    if val < min_val:
      ans = [a_val, b_val]
      min_val = val

ans.sort()
print(*ans)