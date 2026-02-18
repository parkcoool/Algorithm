def solution(lottos, win_nums):
    win_nums_set = set(win_nums)
    lottos_set = set(lottos)
    zero_count = lottos.count(0)
    
    low = len(win_nums_set & lottos_set)
    high = low + zero_count
    
    return [min(6, 7 - high), min(6, 7 - low)]