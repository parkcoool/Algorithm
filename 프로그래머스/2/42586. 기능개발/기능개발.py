from math import ceil

def solution(progresses, speeds):
    ans = []
    start = 0
    
    while start < len(progresses):
        day = ceil(max(100 - progresses[start], 0) / speeds[start])
        for index in range(start, len(progresses)):
            progresses[index] += day * speeds[index]
            
        count = 0
        while start < len(progresses) and progresses[start] >= 100:
            start += 1
            count += 1
        
        if count > 0: ans.append(count)
    
    return ans