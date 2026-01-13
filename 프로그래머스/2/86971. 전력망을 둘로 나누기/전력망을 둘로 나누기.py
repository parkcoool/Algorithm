from collections import defaultdict

def dfs(graph, n, visited=None):
    if visited is None: visited = set()
    visited.add(n)
    count = 1
    for i in range(len(graph)):
        if graph[min(n, i)][max(n, i)] and i not in visited:
            count += dfs(graph, i, visited)
    return count

def solution(n, wires):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for wire in wires:
        graph[min(wire)][max(wire)] = 1    
    
    ans = 100
    for wire in wires:
        graph[min(wire)][max(wire)] = 0
        
        count = dfs(graph, wire[0])
        diff = abs(n - count - count)
        if diff < ans: ans = diff
        
        graph[min(wire)][max(wire)] = 1
        
    return ans