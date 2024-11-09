import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())
links = [tuple(map(int, input().split())) for _ in range(M)]
nodes = {}

for link in links:
  if link[0] not in nodes:
    nodes[link[0]] = set([link[1]])
  else:
    nodes[link[0]].add(link[1])

  if link[1] not in nodes:
    nodes[link[1]] = set([link[0]])
  else:
    nodes[link[1]].add(link[0])
  

visited = set()


def sol(n):
  visited.add(n)
  if n not in nodes:
    return
  for node in nodes[n]:
    if node not in visited:
      sol(node)

ans = 0
for n in range(1, N + 1):
  if n not in visited:
    ans += 1
    sol(n)

print(ans)
