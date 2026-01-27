def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]))
    
    ans = 0
    last_camera = -30001 
    for start, end in routes:
        if start > last_camera:
            ans += 1
            last_camera = end
    
    return ans