def solution(s):
    s1 = []
    
    for i in s :
        if i == "(" :
            s1.append(i)
        else :
            if s1 :
                s1.pop()
            else :
                s1.append(i)
            
    return False if s1 else True