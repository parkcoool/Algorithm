from collections import defaultdict

def solution(gems):
    n = len(gems)
    target = len(set(gems))
    
    counts = defaultdict(int)
    ans = [1, n]
    start = 0
    
    for end in range(n):
        counts[gems[end]] += 1
        
        while len(counts) == target:
            if (end - start) < (ans[1] - ans[0]):
                ans = [start + 1, end + 1]
            
            counts[gems[start]] -= 1
            if counts[gems[start]] == 0:
                del counts[gems[start]]
            start += 1
            
    return ans