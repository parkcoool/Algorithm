def solution(numbers):
    stack = []
    ans = []
    
    for index, num in enumerate(numbers):
        while stack and stack[-1][1] < num:
            past_index, past_num = stack.pop()
            ans.append((past_index, num))
        stack.append((index, num))
        
    result = [-1] * len(numbers)
    for index, num in ans:
        result[index] = num
        
    return result