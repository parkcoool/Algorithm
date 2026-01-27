from copy import deepcopy

def solution(game_board, table):
    S = len(table)
    
    for y in range(S):
        for x in range(S):
            table[y][x] = 1 if table[y][x] == 0 else 0
    
    def get_shape(y, x, grid, origin):
        origin_y, origin_x = origin
        shape = set([(y - origin_y, x - origin_x)])
        for dy, dx in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            new_y, new_x = y + dy, x + dx
            if not (0 <= new_y < S): continue
            if not (0 <= new_x < S): continue
            if grid[new_y][new_x] == 1: continue
            grid[new_y][new_x] = 1
            shape |= get_shape(new_y, new_x, grid, origin)
        return shape
    
    shapes = []
    for y in range(S):
        for x in range(S):
            if game_board[y][x] == 1: continue
            game_board[y][x] = 1
            shape = get_shape(y, x, game_board, [y, x])
            shapes.append(shape)
    
    ans = 0
    for _ in range(4):
        new_table = [[0] * S for _ in range(S)]
        for r in range(S):
            for c in range(S):
                new_table[c][S - 1 - r] = table[r][c]
        table = new_table
        
        for y in range(S):
            for x in range(S):
                if table[y][x] == 1: continue
                backup_table = deepcopy(table)
                table[y][x] = 1
                shape = get_shape(y, x, table, [y, x])
                match = False
                for i in range(len(shapes)):
                    if shapes[i] == shape:
                        shapes.pop(i)
                        ans += len(shape)
                        match = True
                        break
                if not match: table = backup_table
    
    return ans
    