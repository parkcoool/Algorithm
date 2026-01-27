from collections import deque, defaultdict

def solution(n, computers):
    graph = defaultdict(set)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] != 1: continue
            graph[i].add(j)
            graph[j].add(i)
    
    ans = 0
    visited = set()
    for i in range(n):
        if i in visited: continue
        visited.add(i)
        ans += 1
        q = deque([i])
        while q:
            current = q.popleft()
            for next in graph[current]:
                if next in visited: continue
                visited.add(next)
                q.append(next)
    
    return ans