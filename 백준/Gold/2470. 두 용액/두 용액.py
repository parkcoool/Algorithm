import bisect

N = int(input())
nums = sorted(map(int, input().split()))

result = 2_000_000_000
ans = ()
for index in range(N):
    num = nums[index]

    opposite_index = -1
    opposite_indexes = [bisect.bisect_left(nums, -num, hi=index-1), bisect.bisect_left(nums, -num, lo=index+1)]
    opposite_indexes += [opposite_indexes[0] - 1, opposite_indexes[1] - 1]
    
    for i in opposite_indexes:
        if index == i or not (0 <= i < N):
            continue
        if opposite_index == -1 or abs(nums[i] + num) < abs(nums[opposite_index] + num):
            opposite_index = i
    
    opposite = nums[opposite_index]
    add = num + opposite
    if abs(add) < result:
        result = abs(add)
        ans = (min(num, opposite), max(num, opposite))

print(*ans)