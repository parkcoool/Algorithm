import sys

input = sys.stdin.readline

N = int(input())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**(1 / 2)) + 1):
    if is_prime[i]:
        is_prime[i*i : N+1 : i] = [False] * len(is_prime[i*i : N+1 : i])

S = [0]
for num, is_prime in enumerate(is_prime):
  if is_prime: S.append(S[-1] + num)

s, e = 1, 1
ans = 0
while e < len(S):
  value = S[e] - S[s - 1]
  if value == N: ans += 1

  if value >= N:
    s += 1
  else:
    e += 1

print(ans)