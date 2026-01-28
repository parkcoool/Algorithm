from collections import deque

def solution(board):
    N = len(board)
    
    costs = [[[float("inf")] * 4 for _ in range(N)] for _ in range(N)]
    costs[0][0] = [0] * 4
    
    q = deque([(0, 0)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            dy, dx = ((-1, 0), (0, -1), (0, 1), (1, 0))[i]
            new_y, new_x = y + dy, x + dx
            if not(0 <= new_y < N): continue
            if not(0 <= new_x < N): continue
            if board[new_y][new_x] == 1: continue
            
            min_cost = float("inf")
            for j in range(4):
                cost = costs[y][x][j] + 100
                if i != j: cost += 500
                min_cost = min(min_cost, cost)
            
            if min_cost < costs[new_y][new_x][i]:
                costs[new_y][new_x][i] = min_cost
                q.append((new_y, new_x))
    
    return min(costs[N - 1][N - 1])