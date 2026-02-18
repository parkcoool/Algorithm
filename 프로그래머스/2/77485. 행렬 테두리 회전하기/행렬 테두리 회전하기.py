MOVES = { "R": [0, 1], "D": [1, 0], "L": [0, -1], "U": [-1, 0] }

def solution(rows, columns, queries):
    grid = [[0] * (columns + 1)]
    grid += [[0] + list(range(columns * y + 1, columns * (y + 1) + 1)) for y in range(rows)]
    ans = []
    
    for y1, x1, y2, x2 in queries:        
        last = grid[y1 + 1][x1]
        y, x = y1, x1
        direction = "R"
        min_val = last
        
        while True:
            temp = grid[y][x]
            grid[y][x] = last
            last = temp
            min_val = min(min_val, last)
            
            dy, dx = MOVES[direction]
            y, x = y + dy, x + dx
            
            if y > y2:
                direction = "L"
                y, x = y2, x2 - 1
            elif y < y1:
                break
            elif x > x2:
                direction = "D"
                y, x = y1 + 1, x2
            elif x < x1:
                direction = "U"
                y, x = y2 - 1, x1
                
        ans.append(min_val)
    return ans