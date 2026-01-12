from math import ceil

def solution(progresses, speeds):
    day_spends = [ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    
    index = 0
    ans = []
    while index < len(progresses):
        count = 0
        max_day = day_spends[index]
        while index < len(progresses) and day_spends[index] <= max_day:
            index += 1
            count += 1
        if count > 0: ans.append(count)
    
    return ans