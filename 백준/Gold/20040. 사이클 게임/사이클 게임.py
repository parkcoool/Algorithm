import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().strip().split())
parents = list(range(n))

def find(x):
  if parents[x] == x: return x
  parent = find(parents[x])
  parents[x] = parent
  return parent

def union(x, y):
  parent_x = find(x)
  parent_y = find(y)
  
  if parent_x < parent_y:
    parents[parent_x] = parent_y
  else:
    parents[parent_y] = parent_x

def solve():
  ans = 0
  for _ in range(m):
    ans += 1
    
    x, y = map(int, input().strip().split())
    parent_x = find(x)
    parent_y = find(y)
  
    if parent_x == parent_y:
      return ans
  
    union(x, y)
  return 0

print(solve())