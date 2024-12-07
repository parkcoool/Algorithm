import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, start):
    # distances[n]: start에서 n으로 가는 최단 거리
    distances = [float("inf")] * (N + 1)
    distances[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, node = heapq.heappop(q)
        
        if distances[node] < dist: continue
        for next_node in graph[node]:
            next_dist = dist + graph[node][next_node]
            if next_dist >= distances[next_node]: continue
            distances[next_node] = next_dist
            heapq.heappush(q, (next_dist, next_node))

    return distances

N, M, X = map(int, input().split())
graph = {n: {} for n in range(1, N + 1)}
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a][b] = t
    
distances = dijkstra(graph, X)

ans = 0
for i in range(1, N + 1):
    distances[i] += dijkstra(graph, i)[X]
    ans = max(ans, distances[i])

print(ans)