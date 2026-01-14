def dfs(n, graph, visited):
    visited.add(n)
    for i, linked in enumerate(graph[n]):
        if not linked: continue
        if i in visited: continue
        dfs(i, graph, visited)
    

def solution(n, computers):
    visited = set()
    ans = 0
    for i in range(n):
        if i in visited: continue
        dfs(i, computers, visited)
        ans += 1
    return ans