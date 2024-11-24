N = int(input())
nums = sorted(map(int, input().split()))

ans = [1_000_000_000, 1_000_000_000, 1_000_000_000]
for i in range(N):
    start, end = i + 1, N - 1
    while start < end:
        add = nums[i] + nums[start] + nums[end]

        if abs(add) < abs(sum(ans)):
            ans = [nums[i], nums[start], nums[end]]
        if add < 0:
            start += 1
        elif add > 0:
            end -= 1
        else:
            break

print(*ans)