def solution(board):
    H = len(board)
    W = len(board[0])
    
    if H < 2 or W < 2:
        for row in board:
            for num in row:
                if num == 1: return 1
        return 0
    
    max_side = 0
    for i in range(1, H):
        for j in range(1, W):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                max_side = max(max_side, board[i][j])
                
    return max_side ** 2