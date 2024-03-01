def solution(n, lost, reserve):
    s = [1] * (n + 1)
        
    for i in range(1, n+1) :
        if i in lost : s[i] -= 1
        if i in reserve : s[i] += 1
    
    for i in range(1, n+1):
        if s[i] == 0:
            if 0 < i-1 and s[i-1] > 1:
                s[i-1] -= 1
                s[i] += 1
            elif i+1 <= n and s[i+1] > 1:
                s[i+1] -= 1
                s[i] += 1
                
    return len([i for i in s[1:] if i > 0])