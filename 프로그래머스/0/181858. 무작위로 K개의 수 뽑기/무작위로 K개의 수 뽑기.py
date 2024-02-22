def solution(arr, k):
    answer = []
    i = 0
    for i in arr :
        if i not in answer and len(answer) < k:
            answer.append(i)
    
    if len(answer) < k :
        for _ in range(k-len(answer)) :
            answer.append(-1)
        
    return answer