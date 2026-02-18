import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip().split()))
max_num = max(nums)

scores = {num: 0 for num in nums}
for num in nums:
  for multiple in range(num * 2, max_num + 1, num):
    if multiple in scores:
      scores[multiple] -= 1
      scores[num] += 1

for num in nums:
  print(scores[num], end=" ")