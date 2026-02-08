from collections import deque, defaultdict
import sys

input = sys.stdin.readline

for _ in range(int(input())):
  N, K = map(int, input().strip().split())
  D = [0] + list(map(int, input().strip().split()))

  # 그래프 생성
  graph = defaultdict(set)
  indegrees = [0] * (N + 1)
  for _ in range(K):
    a, b = map(int, input().strip().split())
    graph[a].add(b)
    indegrees[b] += 1
    
  W = int(input())

  # 진입점 찾기
  q = deque([])
  for i in range(1, N + 1):
    if indegrees[i] == 0:
      q.append(i)

  # dp[i]: i번 빌딩을 짓기 시작하기 위한 시간
  dp = [0] * (N + 1)
  ans = D[W]

  while q:
    curr = q.popleft()
    time = D[curr] + dp[curr]

    for next in graph[curr]:
      dp[next] = max(dp[next], time)

      indegrees[next] -= 1
      if indegrees[next] == 0:
        q.append(next)

  print(dp[W] + D[W])