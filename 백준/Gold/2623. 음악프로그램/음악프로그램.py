import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

graph = defaultdict(set)
indegrees = [0] * (N + 1)
for _ in range(M):
  order_count, *order = map(int, input().strip().split())
  
  for i, num in enumerate(order):
    if i >= order_count - 1: break
    next_num = order[i + 1]
    if next_num in graph[num]: continue
    graph[num].add(next_num)
    indegrees[next_num] += 1

ans = []
q = deque([i for i in range(1, N + 1) if indegrees[i] == 0])

while q:
  curr = q.popleft()
  ans.append(curr)

  for num in graph[curr]:
    indegrees[num] -= 1
    if indegrees[num] == 0:
      q.append(num)

if len(ans) != N: print(0)
else: print(*ans, sep="\n")