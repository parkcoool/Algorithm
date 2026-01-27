def solution(number, k):
    stack = []
    for num in number:
        while stack and k and int(stack[-1]) < int(num):
            stack.pop()
            k -= 1
        stack.append(num)
    while k:
        stack.pop()
        k -= 1
    return "".join(stack)