import sys

input = sys.stdin.readline

def solution(N, K):
  for i in range(1, int(K ** 0.5) + 1):
    j = K // i
    if i * j != K: continue
    if i + j - 1 != N: continue
    return "YES"
  return "NO"

for _ in range(int(input())):
  N, K = map(int, input().split())
  print(solution(N, K))