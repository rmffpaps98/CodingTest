def solution(clothes):
    answer = 1
    
    cloth = {}
    for i, j in clothes :
        if j in cloth :
            cloth[j] += 1
        else :
            cloth[j] = 1
    
    for i in cloth.values() :
        answer *= (i + 1)
        
    return answer - 1