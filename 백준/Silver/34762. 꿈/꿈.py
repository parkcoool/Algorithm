import sys

input = sys.stdin.readline

def solution():
  N, K = map(int, input().split())
  M = int(input())
  S = list(map(int, input().split()))

  for i, num in enumerate(S):
    if i > 0 and num != S[i - 1] + 1:
      length = num - S[i - 1] - 1
      if length < K + 1: return "NO"
        
  last_length = N - S[-1]
  if 0 < last_length < K + 1: return "NO"

  return "YES"

print(solution())