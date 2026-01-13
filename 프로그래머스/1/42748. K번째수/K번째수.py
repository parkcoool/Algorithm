def solution(array, commands):
    ans = []
    for command in commands:
        i, j, k = command
        ans.append(sorted(array[i - 1: j])[k - 1])
    return ans