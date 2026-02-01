import sys
import heapq

input = sys.stdin.readline

n = int(input())
lines = []

for _ in range(n):
    h, o = map(int, input().split())
    lines.append((min(h, o), max(h, o)))
    
d = int(input())

lines.sort(key=lambda x: x[1])

heap = []
ans = 0

for s, e in lines:
    if e - s > d: continue
    
    heapq.heappush(heap, s)
  
    rail_start = e - d
    while heap and heap[0] < rail_start:
        heapq.heappop(heap)
      
    ans = max(ans, len(heap))
    
print(ans)