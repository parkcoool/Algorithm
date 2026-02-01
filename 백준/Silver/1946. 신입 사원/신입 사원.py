import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  ranks = [tuple(map(int, input().split())) for _ in range(N)]
  ranks.sort(reverse=True)

  ans = N
  stack = []
  for rank1, rank2 in ranks:
    while stack and stack[-1] > rank2:
      stack.pop()
      ans -= 1
    stack.append(rank2)

  print(ans)