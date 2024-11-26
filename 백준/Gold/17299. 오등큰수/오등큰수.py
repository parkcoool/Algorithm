N = int(input())
nums = list(map(int, input().split()))

F = {}
for num in nums:
    if num in F: F[num] += 1
    else: F[num] = 1

ans = [-1] * N
stack = []
for i in range(N):
    while stack and F[nums[stack[-1]]] < F[nums[i]]:
        ans[stack.pop()] = nums[i]
    stack.append(i)

print(*ans)