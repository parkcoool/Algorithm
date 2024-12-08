import sys
import heapq
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
graph = {n: {} for n in range(1, N + 1)}
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a][b] = c

ans = 0

def dfs(x):
    global ans
    
    lengths = []
    for child in graph[x]:
        length = dfs(child)
        heapq.heappush(lengths, -(length + graph[x][child]))

    result = -lengths[0] if lengths else 0
    ans = max(ans, -sum(heapq.nsmallest(2, lengths)))

    return result

dfs(1)
print(ans)