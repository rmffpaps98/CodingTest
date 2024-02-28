def solution(arr):
    r = len(arr)
    c = len(arr[0])
    n = max(r, c)
    answer = [[0] * n for _ in range(n)]
    
    for i in range(len(arr)) :
        for j in range(len(arr[0])) :
            if arr[i][j] :
                answer[i][j] = arr[i][j]
    
    return answer