import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().strip().split())

# (비용, 노드)
graph = defaultdict(list)
for _ in range(E):
  a, b, c = map(int, input().strip().split())
  graph[a].append((c, b))
  graph[b].append((c, a))

pq = [(0, 1)]
visited = [0] * (V + 1)
ans = 0

while pq:
  cost, node = heapq.heappop(pq)
  if visited[node]: continue
  ans += cost
  visited[node] = 1
  for next_cost, next_node in graph[node]:
    if visited[next_node]: continue
    heapq.heappush(pq, (next_cost, next_node))

print(ans)