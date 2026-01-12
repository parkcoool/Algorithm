def solution(arr):
    ans = []
    last = -1
    for num in arr:
        if num != last:
            last = num
            ans.append(num)
    return ans