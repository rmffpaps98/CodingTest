def solution(priorities, location):
    answer = 0
    q = [(i,j) for i, j in enumerate(priorities)]
    
    while True :
        c = q.pop(0)
        if any(c[1] < i[1] for i in q) :
            q.append(c)
        else :
            answer += 1
            if c[0] == location :
                return answer