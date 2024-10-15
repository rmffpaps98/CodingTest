def solution(clothes):
    answer = 1
    c = dict()
    
    for i, j in clothes :
        c[j] = c.get(j, 1) + 1
        
    for i, j in c.items() :
        answer *= j
        
    return answer-1