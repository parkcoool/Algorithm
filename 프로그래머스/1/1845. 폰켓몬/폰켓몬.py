def solution(nums):
    nums_set = set(nums)
    return min(len(nums_set), len(nums) / 2)