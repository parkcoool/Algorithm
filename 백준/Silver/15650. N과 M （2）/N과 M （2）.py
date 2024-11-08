N, M = map(int, input().split())

seq = list(range(1, M + 1))
while True:
  print(" ".join(map(str, seq)))
  if seq[0] == N - M + 1 and seq[-1] == N:
    break
  seq[-1] += 1
  index = M - 1
  while index >= 0:
    if seq[index] > N - (M - index - 1):
      seq[index - 1] += 1
      for i in range(index, M):
        seq[i] = seq[index - 1] + i - index + 1
    index -= 1