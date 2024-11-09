from collections import deque

N = int(input())
tree = {}
for _ in range(N - 1):
  a, b = map(int, input().split())

  if a not in tree:
    tree[a] = [b]
  else:
    tree[a].append(b)

  if b not in tree:
    tree[b] = [a]
  else:
    tree[b].append(a)

queue = deque([1])
ans = [-1] * (N + 1)

while len(queue) > 0:
  current = queue.popleft()

  for node in tree[current]:
    if ans[node] == -1:
      ans[node] = current
      queue.append(node)

for i in range(2, N + 1):
  print(ans[i])
