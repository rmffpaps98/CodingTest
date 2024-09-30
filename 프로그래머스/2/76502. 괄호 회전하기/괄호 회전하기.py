def solution(s):
    answer = 0
    n = len(s)
    
    pairs = {')' : '(', ']' : '[', '}' : '{'}
    
    for i in range(n) :
        stack = []
        ss = s[i:] + s[:i]
        
        for j in ss :
            if j in pairs.values() :
                stack.append(j)
            elif j in pairs :
                if stack and stack[-1] == pairs[j] :
                    stack.pop()
                else :
                    break
            
        else :
            if not stack :
                answer += 1
                    
    return answer