from bisect import bisect_left

def solution(citations):
    nums = sorted(citations)
    for h in range(len(nums), -1, -1):
        count = len(nums) - bisect_left(nums, h)
        if count >= h: return h