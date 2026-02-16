import sys
import heapq

input = sys.stdin.readline

while True:
  input_nums = list(map(int, input().strip().split()))
  N, *nums = input_nums
  if len(nums) == 0: break

  # (-높이, 시작 인덱스)
  pq = []
  ans = 0
  
  for i, num in enumerate(nums):
    current_start = i
    
    while pq and -pq[0][0] > num:
      height, start = heapq.heappop(pq)
      height *= -1
      
      current_start = min(current_start, start)
      ans = max(ans, height * (i - start))

    if not pq or -pq[0][0] < num:
      if num == 0: continue
      heapq.heappush(pq, (-num, current_start))

  while pq:
    height, start = heapq.heappop(pq)
    height *= -1

    ans = max(ans, height * (N - start))
  
  print(ans)