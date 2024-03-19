def solution(m, n, board):
    board = [list(row) for row in board]
    cnt = 0
    
    while True:
        remove_blocks = set()
        
        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                if block != '0' and block == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    remove_blocks |= {(i, j), (i+1, j), (i, j+1), (i+1, j+1)}
        
        if not remove_blocks:
            break
        
        cnt += len(remove_blocks)
        
        for i, j in remove_blocks:
            board[i][j] = '0'
        
        for j in range(n):
            for i in range(m-1, 0, -1):
                if board[i][j] == '0':
                    for k in range(i-1, -1, -1):
                        if board[k][j] != '0':
                            board[i][j], board[k][j] = board[k][j], board[i][j]
                            break
    
    return cnt
