from collections import deque

N, K = map(int, input().split())

# dp[i] = N에서 i까지 가는 데 걸리는 최소 시간
dp = {N: 0}
queue = deque([N])

while len(queue) > 0:
  current = queue.popleft()
  if current == K:
    break
  for next in (current + 1, current - 1, current * 2):
    if 0 <= next <= 100000 and next not in dp:
      dp[next] = dp[current] + 1
      queue.append(next)

print(dp[K])