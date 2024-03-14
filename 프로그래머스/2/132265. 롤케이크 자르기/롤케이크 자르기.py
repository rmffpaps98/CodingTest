def solution(topping):
    answer = 0
    lt = {}
    rt = {}
    
    for i in topping :
        rt[i] = rt.get(i, 0) + 1
        
    for i in topping :
        rt[i] -= 1
        lt[i] = lt.get(i, 0) + 1
        if rt[i] == 0 :
            rt.pop(i)
        if len(lt) == len(rt) :
            answer += 1
        
    return answer