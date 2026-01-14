def solution(numbers, target):
    if len(numbers) == 0:
        return 1 if target == 0 else 0
    
    num = numbers[0]    
    ans = 0
    ans += solution(numbers[1:], target - num)
    ans += solution(numbers[1:], target + num)
    
    return ans