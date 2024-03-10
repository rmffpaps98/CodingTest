def solution(clothes):
    answer = 1
    clo = {}
    
    for _, i in clothes :
        clo[i] = clo.get(i, 0) + 1
             
    for i in clo :
        answer *= clo[i] + 1
        
    return answer - 1