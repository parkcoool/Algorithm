from collections import defaultdict
import heapq

INF = float("inf")

def get_costs(n, graph, start):
    costs = {node: INF for node in range(1, n + 1)}
    costs[start] = 0
    
    q = [(0, start)]    
    while q:
        curr_cost, curr = heapq.heappop(q)
        
        if costs[curr] < curr_cost:
            continue
            
        for next_node, cost in graph[curr]:
            next_cost = curr_cost + cost
            if next_cost < costs[next_node]:
                costs[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))
                
    return costs

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for x, y, cost in fares:
        graph[x].append((y, cost))
        graph[y].append((x, cost))
    
    ans = float("inf")
    
    costs_s = get_costs(n, graph, s)
    costs_a = get_costs(n, graph, a)
    costs_b = get_costs(n, graph, b)
    
    cost_ab = costs_a[b]
    
    for i in range(1, n + 1):
        ans = min(ans, costs_s[i] + costs_a[i] + costs_b[i])
        ans = min(ans, costs_s[i] + costs_a[i] + cost_ab)
        ans = min(ans, costs_s[i] + costs_b[i] + cost_ab)
    
    return ans
        