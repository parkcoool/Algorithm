def solution(n, w, num):
    a = num
    ans = 0
    while a <= n:
        ans += 1
        end = ((a - 1) // w + 1) * w
        a += (end - a) * 2 + 1
    return ans