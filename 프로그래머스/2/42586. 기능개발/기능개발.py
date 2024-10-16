def solution(progresses, speeds):
    answer = []
    cnt = 1
    d = (100 - progresses[0] + speeds[0] - 1) // speeds[0]
    
    for i in range(1, len(progresses)):
        c = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
        
        if c <= d:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            d = c
    
    answer.append(cnt)
    
    return answer