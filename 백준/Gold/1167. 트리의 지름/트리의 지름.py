from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    node, *info, _ = map(int, input().split())
    for i in range(0, len(info), 2):
        graph[node].append((info[i], info[i + 1]))

def bfs(x):
    q = deque([x])
    distances = [-1] * (V + 1)
    distances[x] = 0
    while q:
        current = q.popleft()
        for node, distance in graph[current]:
            if distances[node] != -1: continue
            distances[node] = distances[current] + distance
            q.append(node)
    return distances        

start = 0
result = bfs(1)
for i in range(1, V + 1):
    if result[i] > result[start]:
        start = i
print(max(bfs(start)))