from collections import deque

N, K = map(int, input().split())

# dp[i] = N에서 i까지 가는 최소 시간
dp = {N: 0}
q = deque([N])

while q:
  current = q.popleft()

  if current == K:
    print(dp[K])
    break

  if current <= 50000 and current * 2 not in dp:
    dp[current * 2] = dp[current]
    q.appendleft(current * 2)

  if current > 0 and current - 1 not in dp:
    dp[current - 1] = dp[current] + 1
    q.append(current - 1)
  
  if current < 100000 and current + 1 not in dp:
    dp[current + 1] = dp[current] + 1
    q.append(current + 1)