import sys

input = sys.stdin.readline
INF = float("inf")

N, X = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

ans = INF
for i, a in enumerate(A):
  if i == 0:
    ans = min(ans, max(0, a + X - A[1]), max(0, A[1] + X - a))
  elif i == N - 1:
    ans = min(ans, max(0, a + X - A[-2]), max(0, A[-2] + X - a))
  else:
    l, r = A[i - 1], A[i + 1]
    mid = a
    
    # 내리막
    cost1 = 0
    if mid < r + X:
      cost1 += r + X - mid
      mid = r + X
    if l < mid + X:
      cost1 += mid + X - l
    mid = a

    # 오르막
    cost2 = 0
    if mid < l + X:
      cost2 += l + X - mid
      mid = l + X
    if r < mid + X:
      cost2 += mid + X - r
    mid = a

    # 골짜기
    cost3 = 0
    if l < mid + X:
      cost3 += mid + X - l
    if r < mid + X:
      cost3 += mid + X - r

    # 산
    cost4 = 0
    if mid < l + X:
      cost4 += l + X - mid
      mid = l + X
    if mid < r + X:
      cost4 += r + X - mid

    ans = min(ans, cost1, cost2, cost3, cost4)

print(ans)