import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V, E = map(int, input().strip().split())

# (cost, node)
graph = defaultdict(list)
for _ in range(E):
  a, b, c = map(int, input().strip().split())
  graph[a].append((c, b))
  graph[b].append((c, a))

ans = 0
visited = set()

# (cost, node)
pq = [(0, 1)]
while pq:
  cost, node = heapq.heappop(pq)
  if node in visited: continue
  
  visited.add(node)
  ans += cost

  if len(visited) == V:
    break

  for next_cost, next_node in graph[node]:
    if next_node in visited: continue
    heapq.heappush(pq, (next_cost, next_node))
    
print(ans)