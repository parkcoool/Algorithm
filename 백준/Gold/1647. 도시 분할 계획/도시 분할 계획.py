import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().strip().split())

graph = defaultdict(set)
for _ in range(M):
  a, b, c = map(int, input().strip().split())
  graph[a].add((c, b))
  graph[b].add((c, a))

ans = 0
max_cost = 0

# (비용, 노드)
pq = [(0, 1)]
visited = set()

while pq:
  cost, node = heapq.heappop(pq)

  if node in visited: continue
  visited.add(node)
  ans += cost
  max_cost = max(max_cost, cost)
  
  for next_cost, next_node in graph[node]:
    if next_node in visited: continue
    heapq.heappush(pq, (next_cost, next_node))

ans -= max_cost
print(ans)