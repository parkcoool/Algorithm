import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  graph = [0] + list(map(int, input().strip().split()))

  indegrees = [0] * (N + 1)
  for target in graph:
    indegrees[target] += 1

  q = deque([])
  for i in range(1, N + 1):
    if indegrees[i] == 0:
      q.append(i)

  ans = 0
  while q:
    current = q.popleft()
    ans += 1
    
    next_node = graph[current]
    indegrees[next_node] -= 1
    if indegrees[next_node] == 0:
      q.append(next_node)

  print(ans)