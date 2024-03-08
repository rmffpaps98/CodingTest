def solution(s):
    answer = 0
    for i in range(len(s)) :
        stack = []
        ss = s[i:] + s[:i]
        for j in ss :
            if stack :
                if stack and stack[-1] == "(" and j == ")" :
                    stack.pop()
                elif stack and stack[-1] == "[" and j == "]" :
                    stack.pop()
                elif stack and stack[-1] == "{" and j == "}" :
                    stack.pop()
                else :
                    stack.append(j)
            else :
                stack.append(j)
                
        if not stack :
            answer += 1
    return answer