def solution(babbling):
    answer = 0
    b = []
    
    for i in babbling :
        tmp = i
        for j in ["aya", "ye", "woo", "ma"] :
            if j in tmp :
                tmp = tmp.replace(j, ' ')
        b.append(tmp)
    
    for i in b :
        if not i.strip() : answer += 1
        elif i.strip() in ["aya", "ye", "woo", "ma"] :
            answer += 1
    
    return answer