def solution(s):
    num = 0
    for c in s:
        if c == "(": num += 1
        else: num -= 1
        if num < 0: return False
    if num != 0: return False
    return True