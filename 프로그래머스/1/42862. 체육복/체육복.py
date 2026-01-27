def solution(n, lost, reserve):
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    
    for i in sorted(real_lost):
        if i - 1 in real_reserve:
            real_reserve.remove(i - 1)
        elif i + 1 in real_reserve:
            real_reserve.remove(i + 1)
        else:
            n -= 1
            
    return n