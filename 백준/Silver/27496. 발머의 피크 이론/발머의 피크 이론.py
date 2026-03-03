import sys

input = sys.stdin.readline

N, L = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

# nums_sum[i]: nums[0] ~ nums[i - 1]의 합
nums_sum = [0]
for num in nums:
    nums_sum.append(nums_sum[-1] + num)

ans = 0
for i in range(N):
  alcohol = nums_sum[i + 1] - nums_sum[max(i + 1 - L, 0)]
  if 129 <= alcohol <= 138: ans += 1

print(ans)