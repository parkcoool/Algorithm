N = int(input())
M = int(input())
nums = sorted(map(int, input().split()))

start, end = 0, N - 1
ans = 0
while start != end:
    add = nums[start] + nums[end]
    if add == M: ans += 1

    if add < M: start += 1
    else: end -= 1
print(ans)