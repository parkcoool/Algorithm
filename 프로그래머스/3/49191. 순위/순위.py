def solution(n, results):
    # board[i][j]: i가 j를 이겼는지 여부
    board = [[0] * n for _ in range(n)]
    for winner, loser in results:
        board[winner - 1][loser - 1] = 1
    
    # k: 중간 선수, i: 이긴 선수, j: 진 선수
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][k] == 1 and board[k][j] == 1:
                    board[i][j] = 1
                    
    answer = 0
    for i in range(n):
        count = sum(board[i])
        count += sum([board[j][i] for j in range(n)])
        
        if count == n - 1:
            answer += 1
            
    return answer