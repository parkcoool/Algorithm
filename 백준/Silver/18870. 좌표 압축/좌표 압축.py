from bisect import bisect_left

N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

indicies = set()
for num in nums:
  indicies.add(bisect_left(sorted_nums, num))

indicies = sorted(indicies)
for num in nums:
  print(bisect_left(indicies, bisect_left(sorted_nums, num)), end=" ")