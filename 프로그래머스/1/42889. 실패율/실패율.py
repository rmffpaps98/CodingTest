def solution(N, stages):
    fail = {}
    p = len(stages)
    
    for i in range(1, N+1) :
        if p != 0 :
            fail[i] = stages.count(i) / p
            p -= stages.count(i)
        else :
            fail[i] = 0
    
    return sorted(fail, key=lambda x : fail[x], reverse=True)