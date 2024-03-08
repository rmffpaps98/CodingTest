def solution(k, tangerine):
    answer = 0
    t = {}
    
    for i in tangerine:
        if i in t:
            t[i] += 1
        else:
            t[i] = 1
            
    t = sorted(t.values(), reverse=True)
    
    for i in t:
        answer += 1
        k -= i
        if k <= 0:
            break
            
    return answer