def solution(numLog):
    answer = ''
    prev = numLog[0]
    sim = {1 : "w", -1 : "s", 10 : "d", -10 : "a"}
    for i in numLog[1:] :
        if prev != i :
            answer += sim[i-prev]
        prev = i        
    return answer