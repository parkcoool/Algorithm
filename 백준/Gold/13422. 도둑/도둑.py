import sys

input = sys.stdin.readline

for _ in range(int(input().strip())):
  N, M, K = map(int, input().strip().split())
  money = list(map(int, input().strip().split()))

  ans = 0
  total_money = sum(money[:M])
  for i in range(N):
    if total_money < K: ans += 1

    if N == M: break

    # money[i] + ... + money[j]
    j = (i + M) % N
    total_money += money[j]
    total_money -= money[i]

  print(ans)