def solution(board, moves):
    answer = 0
    n = len(board)
    arr = []
    
    for i in moves :
        for j in range(len(board)) :
            if arr and len(arr) > 1 and arr[-1] == arr[-2] :
                arr.pop()
                arr.pop()
                answer += 2
                
            if board[j][i-1] :
                arr.append(board[j][i-1])
                board[j][i-1] = 0
                break
            
    return answer