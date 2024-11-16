N = int(input())
nums = [int(input()) for _ in range(N)]

ans = []
stack = []
new_num = 1
for num in nums:
    while new_num <= num:
        stack.append(new_num)
        new_num += 1
        ans.append("+")

    if stack and stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        exit()

for sign in ans:
    print(sign)