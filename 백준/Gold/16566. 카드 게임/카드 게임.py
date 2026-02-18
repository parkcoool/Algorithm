import sys
from bisect import bisect_right

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, K = map(int, input().strip().split())

cards = list(map(int, input().strip().split()))
cards.sort()

cheolsus = list(map(int, input().strip().split()))

parents = list(range(M))

def find(x):
  if parents[x] == x: return x
  parent = find(parents[x])
  parents[x] = parent
  return parent

def union(x, y):
  parent_x = find(x)
  parent_y = find(y)

  if parent_x > parent_y:
    parents[parent_y] = parent_x
  else:
    parents[parent_x] = parent_y

for cheolsu in cheolsus:
  index = bisect_right(cards, cheolsu)
  index = min(find(index), M - 1)
  minsu = cards[index]

  if index + 1 < M:
    union(index, index + 1)

  print(minsu)