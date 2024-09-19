def solution(k, tangerine):
    answer = 0
    
    tan_d = {}
    for i in tangerine:
        if i in tan_d:
            tan_d[i] += 1
        else:
            tan_d[i] = 1
    
    tan_d = sorted(tan_d.items(), key=lambda x: x[1], reverse=True)
    
    for size, count in tan_d:
        if k > 0:
            k -= count
            answer += 1
        else :
            break
    
    return answer
