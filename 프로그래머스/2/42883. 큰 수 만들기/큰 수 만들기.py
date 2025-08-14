def solution(number, k):
    s = []
    
    for i in number:
        while k > 0 and s and s[-1] < i:
            s.pop()
            k -= 1
            
        s.append(i)
        
    if k > 0:
        s = s[:-k]
        
    return ''.join(s)