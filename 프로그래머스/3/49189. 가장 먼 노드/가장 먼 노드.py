from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(set)
    for a, b in edge:
        graph[a].add(b)
        graph[b].add(a)
    
    dists = [-1] * (n + 1)
    dists[1] = 0
    
    q = deque([1])
    while q:
        node = q.popleft()
        dist = dists[node]
        for next_node in graph[node]:
            if dists[next_node] != -1: continue
            dists[next_node] = dist + 1
            q.append(next_node)
    
    return dists.count(max(dists))
    