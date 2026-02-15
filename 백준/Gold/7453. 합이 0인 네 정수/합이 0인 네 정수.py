import sys

input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
  a, b, c, d = map(int, input().strip().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

cd_counter = {}
for i in range(N):
  for j in range(N):
    num = C[i] + D[j]
    if num in cd_counter:
      cd_counter[num] += 1
    else:
      cd_counter[num] = 1

ans = 0
for i in range(N):
  for j in range(N):
    num = A[i] + B[j]
    ans += cd_counter.get(-num, 0)

print(ans)