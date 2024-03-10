def solution(cacheSize, cities):
    answer = 0   
    c = []
    
    if cacheSize == 0 : return len(cities) * 5
    
    for i in cities :
        i = i.lower()
        if i in c :
            answer += 1
            c.remove(i)
        else :
            answer += 5
            if len(c) >= cacheSize :
                c.pop(0)
        c.append(i)
    return answer


