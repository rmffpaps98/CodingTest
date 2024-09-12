def solution(s):
    stack = []
    for i in s :
        if stack and i == stack[-1] :
            stack.pop()
        else :
            stack.append(i)

    return int(not len(stack))
