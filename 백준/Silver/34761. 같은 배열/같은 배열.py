import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A != B[:N]: print("NO")
else:
  if set(A) | set(B) == set(A): print("YES")
  else: print("NO")