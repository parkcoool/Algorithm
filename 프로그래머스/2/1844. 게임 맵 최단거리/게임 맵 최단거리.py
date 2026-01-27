from collections import deque

def solution(maps):
    height = len(maps)
    width = len(maps[0])
    
    maps[0][0] = 0
    q = deque([(0, 0, 1)])
    while q:
        y, x, dist = q.popleft()
        if y == height - 1 and x == width - 1: return dist
        for dy, dx in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            new_y, new_x = y + dy, x + dx;
            if not (0 <= new_y < height): continue
            if not (0 <= new_x < width): continue
            if maps[new_y][new_x] == 0: continue
            maps[new_y][new_x] = 0
            q.append((new_y, new_x, dist + 1))
            
    return -1