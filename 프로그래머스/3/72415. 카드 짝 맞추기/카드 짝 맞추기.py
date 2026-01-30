from collections import deque
from itertools import permutations, product

INF = float("inf")

def get_cost(start, end, board):
    if start == end:
        return 0
        
    q = deque([(start[0], start[1], 0)])
    visited = { start }
    
    while q:
        y, x, cost = q.popleft()
        
        for dy, dx in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            # 방향키로 이동
            ny, nx = y + dy, x + dx
            if not (0 <= ny < 4 and 0 <= nx < 4): continue
            
            if (ny, nx) == end:
                return cost + 1
            if (ny, nx) not in visited:
                visited.add((ny, nx))
                q.append((ny, nx, cost + 1))
            
            # Ctrl 키를 누르고 이동
            cy, cx = y, x
            while True:
                ny, nx = cy + dy, cx + dx
                if not (0 <= ny < 4 and 0 <= nx < 4): break
                cy, cx = ny, nx
                if board[cy][cx] != 0: break
            
            if (cy, cx) == end:
                return cost + 1
            if (cy, cx) not in visited:
                visited.add((cy, cx))
                q.append((cy, cx, cost + 1))
                
    return INF

def solution(board, r, c):
    char_points = {}
    for y in range(4):
        for x in range(4):
            if board[y][x]:
                if board[y][x] not in char_points:
                    char_points[board[y][x]] = []
                char_points[board[y][x]].append((y, x))
    
    chars = list(char_points.keys())
    ans = INF

    for char_order in permutations(chars):
        for order in product((0, 1), repeat=len(chars)):
            temp_board = [row[:] for row in board]
            total_dist = 0
            curr_r, curr_c = r, c
            
            for i, char in enumerate(char_order):
                card1 = char_points[char][order[i]]
                card2 = char_points[char][1 - order[i]]
                
                dist1 = get_cost((curr_r, curr_c), card1, temp_board)
                total_dist += dist1 + 1
                temp_board[card1[0]][card1[1]] = 0 # 카드 삭제
                
                dist2 = get_cost(card1, card2, temp_board)
                total_dist += dist2 + 1
                temp_board[card2[0]][card2[1]] = 0 # 카드 삭제
                
                curr_r, curr_c = card2
                
                if total_dist >= ans:
                    break
            
            ans = min(ans, total_dist)
            
    return ans