def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    
    lost_reserve = lost & reserve
    lost -= lost_reserve
    reserve -= lost_reserve
    
    ans = n - len(lost)
    given = set()
    
    for n in lost:
        if n in reserve:
            reserve.remove(n)
            given.add(n)
            ans += 1
        elif n - 1 in reserve and n + 1 not in reserve:
            reserve.remove(n - 1)
            given.add(n - 1)
            ans += 1
        elif n - 1 not in reserve and n + 1 in reserve:
            reserve.remove(n + 1)
            given.add(n + 1)
            ans += 1
    
    for n in lost - given:
        if n - 1 in reserve:
            reserve.remove(n - 1)
            ans += 1
        elif n + 1 in reserve:
            reserve.remove(n + 1)
            ans += 1
        
    return ans
        