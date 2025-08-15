def solution(storey):
    answer = 0
    s = list(str(storey))
    s = s[::-1]
    c = False
    
    for i in range(len(s)):
        if c:
            n = int(s[i]) + 1
            c = False
        else:
            n = int(s[i])
        
        if n == 10:
            c = True
        elif n > 5:
            answer += 10 - n
            c = True
        elif n == 5:
            answer += 5
            next_d = (int(s[i+1]) if i+1 < len(s) else 0)
            c = (next_d >= 5)
        else:
            answer += n
    
    if c:
        return answer + 1
    else:
        return answer