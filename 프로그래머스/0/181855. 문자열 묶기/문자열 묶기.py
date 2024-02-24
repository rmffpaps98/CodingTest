def solution(strArr):
    ln = []
    answer = []
    for i in strArr :
        ln.append(len(i))
    
    for i in set(ln) :
        answer.append(ln.count(i))
        
    return max(answer)