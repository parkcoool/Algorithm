import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(x, depth = 1):
    if depth >= 5:
        print(1)
        exit()
    
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            dfs(node, depth + 1)
    visited[x] = False

visited = [False] * N
ans = False
for i in range(N):
    if i in visited: continue
    dfs(i)
    
print(0)