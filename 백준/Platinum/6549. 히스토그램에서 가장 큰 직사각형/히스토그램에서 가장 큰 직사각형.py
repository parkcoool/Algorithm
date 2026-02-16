import sys

input = sys.stdin.readline

while True:
  input_nums = list(map(int, input().strip().split()))
  N, *nums = input_nums
  if len(nums) == 0: break

  # (-높이, 시작 인덱스)
  stack = []
  ans = 0
  
  for i, num in enumerate(nums):
    current_start = i
    
    while stack and stack[-1][0] > num:
      height, start = stack.pop()
      current_start = min(current_start, start)
      ans = max(ans, height * (i - start))

    if not stack or stack[-1][0] < num:
      if num == 0: continue
      stack.append((num, current_start))

  while stack:
    height, start = stack.pop()
    ans = max(ans, height * (N - start))
  
  print(ans)