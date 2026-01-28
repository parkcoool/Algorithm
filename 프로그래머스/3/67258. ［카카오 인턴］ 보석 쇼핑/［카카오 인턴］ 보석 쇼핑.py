from collections import defaultdict

def solution(gems):
    n = len(gems)
    target = len(set(gems))

    counts = defaultdict(int)
    type_count = 0
    start = 1
    ans = [1, len(gems)]

    for end in range(1, n + 1):
        counts[gems[end - 1]] += 1
        if counts[gems[end - 1]] == 1: type_count += 1
        
        if type_count >= target:
            while type_count >= target:
                counts[gems[start - 1]] -= 1
                if counts[gems[start - 1]] == 0: type_count -= 1
                start += 1
        
            if type_count < target:
                start -= 1
                counts[gems[start - 1]] += 1
                if counts[gems[start - 1]] == 1: type_count += 1
        
        
        if end - start < ans[1] - ans[0] and type_count == target:
            ans = [start, end]
            
    return ans