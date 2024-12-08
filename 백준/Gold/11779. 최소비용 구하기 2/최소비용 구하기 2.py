import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = {n: {} for n in range(N)}

for _ in range(M):
    start, dest, cost = map(int, input().split())
    start, dest = start - 1, dest - 1
    if dest in graph[start]: graph[start][dest] = min(graph[start][dest], cost)
    else: graph[start][dest] = cost
        
start, dest = map(lambda x: int(x) - 1, input().split())

costs = [float("inf")] * N
costs[start] = 0
q = []
heapq.heappush(q, (0, start))
prevs = [0] * N

while q:
    cost, node = heapq.heappop(q)
    if costs[node] < cost: continue
    for next_node in graph[node]:
        next_cost = cost + graph[node][next_node]
        if next_cost >= costs[next_node]: continue
        costs[next_node] = next_cost
        prevs[next_node] = node
        heapq.heappush(q, (next_cost, next_node))

print(costs[dest])

ans = []
node = dest
while node != start:
    ans.append(node + 1)
    node = prevs[node]
ans.append(start + 1)

print(len(ans))
print(*ans[::-1])