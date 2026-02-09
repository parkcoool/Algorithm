import sys
from collections import defaultdict, deque
import heapq

input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = defaultdict(list)

indegrees = [0] * (N + 1)
for _ in range(M):
  a, b = map(int, input().strip().split())
  graph[a].append(b)
  indegrees[b] += 1

pq = [num for num in range(1, N + 1) if indegrees[num] == 0]
heapq.heapify(pq)

while pq:
  num = heapq.heappop(pq)
  print(num, end=" ")
  for next_num in graph[num]:
    indegrees[next_num] -= 1
    if indegrees[next_num] == 0:
      heapq.heappush(pq, next_num)