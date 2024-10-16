def solution(priorities, location):
    answer = 0
    a = [(idx, i) for idx, i in enumerate(priorities)]
    
    while True:
        c = a.pop(0)
        
        if any(c[1] < i[1] for i in a):
            a.append(c)
        else:
            answer += 1
            if c[0] == location:
                return answer
