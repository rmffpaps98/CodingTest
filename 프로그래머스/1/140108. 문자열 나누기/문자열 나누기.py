def solution(s):
    answer = 1
    scnt = 0
    cnt = 0
    tmp = s[0]
    
    for i, j in zip(s, s[1:]) :
        if tmp == i :
            scnt += 1
        elif tmp != i :
            cnt += 1
        
        if scnt == cnt :
            answer += 1
            scnt, cnt = 0, 0
            tmp = j
    return answer