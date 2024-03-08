def solution(elements):
    e = set()
    l = len(elements)
    
    for i in range(l):
        s = 0
        for j in range(i, l + i):
            s += elements[j % l]
            e.add(s)
            
    return len(e)