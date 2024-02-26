def solution(dots):
    line = []
    
    for i in range(len(dots)) :
        d1 = dots[i]
        for d2 in dots[i+1:] :
            l = abs(d1[1] - d2[1]) / abs(d1[0] - d2[0])
            line. append(l)
    
    if line[0] == line[-1] or line[1] == line[-2] or line[2] == line[-3] :
        return 1
    
    return 0
        