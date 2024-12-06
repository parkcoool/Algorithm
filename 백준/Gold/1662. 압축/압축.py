S = input()

ans = 0
stack = [1]
for i in range(len(S)):
    if S[i] == ")":
        stack.pop()
    elif S[i] == "(":
        continue
    elif i == len(S) - 1 or i < len(S) - 1 and S[i + 1] != "(":
        ans += stack[-1]
    else:
        stack.append(stack[-1] * int(S[i]))

print(ans)