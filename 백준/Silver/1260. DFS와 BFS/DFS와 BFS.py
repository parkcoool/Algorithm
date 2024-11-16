import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = {x: set() for x in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

for i in range(1, N + 1):
    graph[i] = sorted(graph[i])

def dfs(x):
    visited.add(x)
    print(x, end=" ")
    for node in graph[x]:
        if node not in visited:
            dfs(node)

def bfs(x):
    q = deque([x])
    while q:
        current = q.popleft()
        print(current, end=" ")
        for node in graph[current]:
            if node not in visited:
                visited.add(node)
                q.append(node)
    

visited = set([V])
dfs(V)
print()
visited = set([V])
bfs(V)