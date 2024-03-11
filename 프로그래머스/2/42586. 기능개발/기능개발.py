def solution(progresses, speeds):
    answer = []
    day = []
    
    for i, j in zip(progresses, speeds) :
        d = 0
        while i < 100 :
            d += 1
            i += j
        day.append(d)
        
    prev = day[0]
    c = 1
    for i in day[1:] :
        if i <= prev :
            c += 1
        else :
            answer.append(c)
            c = 1
            prev = i
            
    answer.append(c)
    return answer