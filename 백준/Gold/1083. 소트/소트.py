N = int(input())
A = list(map(int, input().split()))
S = int(input())

for i in range(N - 1):
  max_index = i
  for j in range(i + 1, min(N, i + 1 + S)):
    if A[j] > A[max_index]:
      max_index = j
  if max_index == i:
    continue
  A = A[:i] + [A[max_index]] + A[i:max_index] + A[max_index + 1:]
  S-= max_index - i

  if S == 0:
    break

print(" ".join(map(str, A)))