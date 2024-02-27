def solution(s):
    answer = []
    
    for idx, i in enumerate(list(s)) :
        if i in s[:idx] :
            cnt = s[:idx].rindex(i)
            answer.append(idx - cnt)
        else :
            answer.append(-1)
    return answer