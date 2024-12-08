import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = {v: {} for v in range(1, V + 1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u]: graph[u][v] = min(graph[u][v], w)
    else: graph[u][v] = w

costs = [float("inf")] * (V + 1)
costs[K] = 0
q = []
heapq.heappush(q, (0, K))

while q:
    cost, node = heapq.heappop(q)
    if cost > costs[node]: continue

    for next_node in graph[node]:
        next_cost = cost + graph[node][next_node]
        if next_cost >= costs[next_node]: continue
        costs[next_node] = next_cost
        heapq.heappush(q, (next_cost, next_node))

for i in range(1, V + 1): print(str(costs[i]).upper())