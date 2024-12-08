import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = {n: {} for n in range(1, N + 1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
v1, v2 = map(int, input().split())

def dijkstra(start, dest):
    dists = [float("inf")] * (N + 1)
    dists[start] = 0
    q = [(0, start)]
    while q:
        dist, node = heapq.heappop(q)
        if dists[node] < dist: continue
        for next_node in graph[node]:
            next_dist = dist + graph[node][next_node]
            if dists[next_node] <= next_dist: continue
            dists[next_node] = next_dist
            heapq.heappush(q, (next_dist, next_node))
    return dists[dest]

ans = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
ans = min(ans, dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))

print(-1 if ans == float("inf") else ans)