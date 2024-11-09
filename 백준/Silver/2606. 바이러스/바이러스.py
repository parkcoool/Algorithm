N = int(input())
P = int(input())
pairs = set([tuple(map(int, input().split())) for _ in range(P)])

visited = set()


def dfs(n):
  visited.add(n)
  result = 1
  for p in pairs:
    if p[0] == n and p[1] not in visited:
      result += dfs(p[1])
    elif p[1] == n and p[0] not in visited:
      result += dfs(p[0])
  return result


print(dfs(1) - 1)
