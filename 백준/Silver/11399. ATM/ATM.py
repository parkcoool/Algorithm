N = int(input())
P = sorted(map(int, input().split()))
ans = 0
add = 0

for p in P:
  ans += add + p
  add += p

print(ans)