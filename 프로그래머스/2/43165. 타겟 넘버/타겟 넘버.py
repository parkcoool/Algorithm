def solution(numbers, target):
    def dfs(index, number):
        if index == len(numbers):
            if number == target: return 1
            else: return 0
        
        result = dfs(index + 1, number + numbers[index])
        result += dfs(index + 1, number - numbers[index])
        return result
        
    return dfs(0, 0)