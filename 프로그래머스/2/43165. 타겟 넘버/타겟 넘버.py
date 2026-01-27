from itertools import product

def solution(numbers, target):
    ans = 0
    for operations in product(["+", "-"], repeat=len(numbers)):
        num = 0
        for i in range(len(numbers)):
            num += numbers[i] * (1 if operations[i] == "+" else -1)
        if num == target: ans += 1
    return ans