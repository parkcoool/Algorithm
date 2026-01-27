def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]))
    
    ans = 0
    visited = set()
    for i1, (s1, e1) in enumerate(routes):
        if i1 in visited: continue
        visited.add(i1)
        ans += 1
        for i2, (s2, e2) in enumerate(routes):
            if i2 in visited: continue
            if s2 <= e1: visited.add(i2)
    
    return ans