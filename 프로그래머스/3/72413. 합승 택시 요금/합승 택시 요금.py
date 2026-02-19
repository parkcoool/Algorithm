from collections import defaultdict
import heapq

INF = float("inf")

def get_costs(graph, a):
    costs = defaultdict(lambda: INF)
    costs[a] = 0
    
    # (cost, node)
    pq = [(0, a)]
    while pq:
        curr_cost, curr_node = heapq.heappop(pq)
        if curr_cost > costs[curr_node]: continue
        
        for next_node, weight in graph[curr_node]:
            next_cost = curr_cost + weight
            if next_cost >= costs[next_node]: continue
            heapq.heappush(pq, (next_cost, next_node))
            costs[next_node] = next_cost
    
    return costs

def solution(n, s, a, b, fares):
    # (node, weight)
    graph = defaultdict(list)
    for x, y, weight in fares:
        graph[x].append((y, weight))
        graph[y].append((x, weight))
    
    ans = INF
    costs_s = get_costs(graph, s)
    costs_a = get_costs(graph, a)
    costs_b = get_costs(graph, b)
    
    for i in range(1, n + 1):
        cost = costs_s[i] + costs_a[i] + costs_b[i]
        ans = min(ans, cost)

    return(ans)
        