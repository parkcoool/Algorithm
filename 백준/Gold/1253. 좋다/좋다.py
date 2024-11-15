N = int(input())
nums = sorted(map(int, input().split()))

ans = 0
for i in range(N):
    num = nums[i]
    start, end = 0, N - 1
    while start < end:
        add = nums[start] + nums[end]
        if add == num:
            if start != i and end != i:
                ans += 1
                break
            elif start == i:
                start += 1
            else:
                end -= 1
        elif add < num:
            start += 1
        else:
            end -= 1
print(ans)