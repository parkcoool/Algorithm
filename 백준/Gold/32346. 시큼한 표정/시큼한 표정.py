import sys

input = sys.stdin.readline
MOD = 1_000_000_007

N = int(input())
string = input().strip() + ">"

fact = [1] * (N + 1)
for i in range(1, N + 1):
  fact[i] = (fact[i - 1] * i) % MOD

inv = [1] * (N + 1)
inv[N] = pow(fact[N], MOD - 2, MOD)
for i in range(N - 1, -1, -1):
  inv[i] = (inv[i + 1] * (i + 1)) % MOD

def nCr_mod(n, r):
  if r < 0 or r > n: return 0
  num = fact[n]
  den = (inv[r] * inv[n - r]) % MOD
  return (num * den) % MOD

chunks = []
l, r = 0, 0

for i, char in enumerate(string):
  if char == ">":
    if l > 0 and r > 0:
      size = min(l, r)
      chunks.append((i - size * 2, size))
      r = 0
    r += 1
    l = 0
  else:
    l += 1
    if l >= r > 0:
      chunks.append((i - l * 2 + 1, l))
      l = 0
      r = 0

ans = 0
for i, size in chunks:
  for j in range(size):
      ways = nCr_mod(N - (size - j) * 2, i + j)
      ans = (ans + ways) % MOD

print(ans)