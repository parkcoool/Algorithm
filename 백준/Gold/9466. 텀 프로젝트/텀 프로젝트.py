import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  graph = [0] + list(map(int, input().strip().split()))

  indegrees = [0] * (N + 1)
  for target in graph[1:]:
    indegrees[target] += 1

  ans = 0
  q = deque([i for i in range(1, N + 1) if indegrees[i] == 0])
  while q:
    current = q.popleft()
    next_node = graph[current]
    ans += 1

    indegrees[next_node] -= 1
    if indegrees[next_node] == 0:
      q.append(next_node)

  print(ans)