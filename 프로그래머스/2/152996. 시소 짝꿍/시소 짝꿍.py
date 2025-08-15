def solution(weights):
    answer = 0
    dw = {}
    
    for i in weights:
        dw[i] = dw.get(i, 0) + 1
    
    for i, j in dw.items():
        if j > 1:
            answer += (j * (j - 1) // 2)
            
        answer += dw[i] * dw.get(i*2, 0)
        
        if (i * 3) % 2 == 0:
            t = (i * 3) // 2
            answer += dw[i] * dw.get(t, 0)
        
        if (i * 4) % 3 == 0:
            t = (i * 4) // 3
            answer += dw[i] * dw.get(t, 0)
                
    return answer