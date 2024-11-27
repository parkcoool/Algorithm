import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
indegrees = [0] * (N + 1)
zero_indegress = set(range(1, N + 1))

graph = {}
for _ in range(M):
    a, b = map(int, input().split())
    indegrees[b] += 1
    zero_indegress.discard(b)
    if a in graph:
        graph[a].add(b)
    else:
        graph[a] = set([b])
        
ans = []
q = deque(zero_indegress)
while q:
    current = q.popleft()
    ans.append(current)

    if current not in graph: continue
    for next in graph[current]:
        indegrees[next] -= 1
        if indegrees[next] == 0:
            q.append(next)

print(*ans)