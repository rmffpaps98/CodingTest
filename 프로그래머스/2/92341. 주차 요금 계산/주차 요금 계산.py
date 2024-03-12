import math

def solution(fees, records):
    answer = []
    bt, bf, pm, pf = fees
    d = {}
    mt = 23*60 + 59
    
    for i in records :
        t, n, e = i.split()
        h, m = t.split(':')
        time = int(h)*60 + int(m)
        if e == 'IN' :
            d[n] = d.get(n, 0) + time
        else :
            d[n] -= time
            
    for i, j in d.items():
        if j >= 0 :
            d[i] -= mt
        
    d = sorted(d.items(), key=lambda x:x[0])
    
    for _, j in d :
        if abs(j) > bt :
            answer.append(bf + math.ceil((abs(j) - bt) / pm) * pf)
        else :
            answer.append(bf)
        
    return answer