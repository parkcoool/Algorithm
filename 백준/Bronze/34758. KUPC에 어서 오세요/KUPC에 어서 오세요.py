import sys

input = sys.stdin.readline

X, Y = map(int, input().split())
N = int(input())

for _ in range(N):
  x, y = map(int, input().split())
  if x == X or y == Y: print(0)
  else: print(1)