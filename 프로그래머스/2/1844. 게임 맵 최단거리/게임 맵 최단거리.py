from collections import deque

def solution(maps):
    height = len(maps)
    width = len(maps[0])
    
    q = deque([(1, 0, 0)])
    visited = set()
    while q:
        dist, y, x = q.popleft()
        
        if y == height - 1 and x == width - 1:
            return dist
        
        for new_y, new_x in ((y + 1, x), (y, x + 1), (y, x - 1), (y - 1, x)):
            if not (0 <= new_y < height and 0 <= new_x < width): continue
            if maps[new_y][new_x] == 0: continue
            if (new_y, new_x) in visited: continue
            visited.add((new_y, new_x))
            q.append((dist + 1, new_y, new_x))
    
    return -1