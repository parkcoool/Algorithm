from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(set)
    for a, b in edge:
        graph[a].add(b)
        graph[b].add(a)
    
    dists = [-1] * (n + 1)
    dists[1] = 0
    
    # (node, dist)
    q = deque([(1, 0)])
    while q:
        node, dist = q.popleft()
        for next_node in graph[node]:
            if dists[next_node] != -1 and dist + 1 >= dists[next_node]: continue
            dists[next_node] = dist + 1
            q.append((next_node, dist + 1))
    
    return dists.count(max(dists))
    