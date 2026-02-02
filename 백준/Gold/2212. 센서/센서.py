import sys
from math import ceil

input = sys.stdin.readline

N = int(input())
K = int(input())
targets = list(map(int, input().strip().split()))
targets.sort()

target_diffs = [0]
for i in range(1, N):
  diff = targets[i] - targets[i - 1]
  target_diffs.append(diff)
target_diffs.sort(reverse=True)

total_length = targets[-1] - targets[0]
print(total_length - sum(target_diffs[:K - 1]))