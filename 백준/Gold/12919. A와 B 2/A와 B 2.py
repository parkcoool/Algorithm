import sys
from collections import deque

input = sys.stdin.readline

S = input().strip()
T = input().strip()
def solution():
  q = deque([T])
  while q:
    word = q.popleft()
    if word == S: return 1
    if len(word) <= len(S): continue
    
    if word[0] == "B":
      q.append(word[::-1][:-1])
    if word[-1] == "A":
      q.append(word[:-1])
  return 0

print(solution())