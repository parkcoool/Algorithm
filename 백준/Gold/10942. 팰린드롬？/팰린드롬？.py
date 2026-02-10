import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().strip().split()))

dp = [[0] * N for _ in range(N)]
for i in range(N):
  # 홀수 자리
  s, e = i, i
  while s >= 0 and e <= N - 1:
    s_num, e_num = seq[s], seq[e]
    if s_num != e_num: break
    dp[s][e] = 1
    s -= 1
    e += 1

  # 짝수 자리
  if i < N - 1:
    s, e = i, i + 1
    while s >= 0 and e <= N - 1:
      s_num, e_num = seq[s], seq[e]
      if s_num != e_num: break
      dp[s][e] = 1
      s -= 1
      e += 1

for _ in range(int(input())):
  s, e = map(int, input().strip().split())
  print(dp[s - 1][e - 1])