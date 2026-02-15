import sys
from bisect import bisect_left, bisect_right
from collections import Counter

input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
  a, b, c, d = map(int, input().strip().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

AB, CD = [], []
for i in range(N):
  for j in range(N):
    AB.append(A[i] + B[j])
    CD.append(C[i] + D[j])

cd_counter = Counter(CD)

ans = 0
for ab in AB:
  ans += cd_counter[-ab]

print(ans)