def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    lost_reserve = lost & reserve
    lost -= lost_reserve
    reserve -= lost_reserve
    
    for i in range(1, n + 1):
        if i not in lost: continue
        if i - 1 in reserve and i + 1 not in reserve:
            reserve.remove(i - 1)
            lost.remove(i)
        elif i - 1 not in reserve and i + 1 in reserve:
            reserve.remove(i + 1)
            lost.remove(i)
    
    for i in range(1, n + 1):
        if i not in lost: continue
        if i - 1 in reserve:
            reserve.remove(i - 1)
            lost.remove(i)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            lost.remove(i)
    
    return n - len(lost)