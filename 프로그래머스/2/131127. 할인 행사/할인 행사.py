def solution(want, number, discount):
    answer = 0
    wn = {i : j for i, j in zip(want, number)}
    n = len(discount)
    
    current_window = {}
    for i in discount[:10] :
        if i in current_window :
            current_window[i] += 1
        else :
            current_window[i] = 1
            
    if current_window == wn :
        answer += 1
        
    for i in range(10, n) :
        if discount[i - 10] in current_window :
            current_window[discount[i - 10]] -= 1
            if current_window[discount[i - 10]] == 0 :
                del current_window[discount[i - 10]]
                
        if discount[i] in current_window :
            current_window[discount[i]] += 1
        else :
            current_window[discount[i]] = 1
            
        if current_window == wn:
            answer += 1
            
    return answer