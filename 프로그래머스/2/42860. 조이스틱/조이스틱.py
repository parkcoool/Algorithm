from math import ceil

def solution(name):
    n = len(name)
    
    ans = n - 1
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == "A":
            next_i += 1
            
        dist1 = i * 2 + n - next_i
        dist2 = i + (n - next_i) * 2
        ans = min(ans, dist1, dist2)
    
    for c in name:
        ans += min(ord(c) - ord("A"), ord("Z") - ord(c) + 1)
    
    return ans