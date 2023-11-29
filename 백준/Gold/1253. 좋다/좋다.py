from bisect import bisect_left


def bi_search(arr, target, lo=0, hi=None):
    if hi == None:
        hi = len(arr)
    result = bisect_left(arr, target, lo, hi)
    if result < hi and arr[result] == target:
        return result
    else:
        return -1


N = int(input())
nums = sorted(map(int, input().split()))

answer = 0
for i in range(N):
    is_good = False
    for j in range(N):
        if i == j:
            continue

        small = nums[j]
        large = nums[i] - small
        large_idx = bi_search(nums, large)

        if large_idx == -1:
            continue

        while large_idx < N and nums[large_idx] == large:
            if large_idx != i and large_idx != j:
                is_good = True
                break  
            large_idx += 1
        
        if is_good:
            answer += 1
            break


print(answer)
