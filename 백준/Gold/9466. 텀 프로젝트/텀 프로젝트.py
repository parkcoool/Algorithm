import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  graph = [0] + list(map(int, input().strip().split()))
  visited = [False] * (N + 1)

  def dfs(node, path):
    visited[node] = True
    path.append(node)
    
    next_node = graph[node]
    
    if visited[next_node]:
      if next_node in path:
        return len(path) - path.index(next_node)
      else:
        return 0
    else:
      return dfs(next_node, path)

  ans = N
  for i in range(1, N + 1):
    if visited[i]: continue
    ans -= dfs(i, [])

  print(ans)