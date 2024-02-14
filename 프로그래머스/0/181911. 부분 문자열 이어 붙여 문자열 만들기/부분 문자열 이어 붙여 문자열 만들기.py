def solution(my_strings, parts):
    answer = ''
    for s, e in parts :
        ms = my_strings.pop(0)
        answer += ms[s:e+1]
    return answer