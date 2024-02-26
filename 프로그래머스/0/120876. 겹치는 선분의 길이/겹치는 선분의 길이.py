def solution(lines):
    answer = []
    num = 0
    for i in lines :
        answer.append(list(range(i[0], i[1])))
    a = set(answer[0])
    b = set(answer[1])
    c = set(answer[2])
    return len(a&b|b&c|a&c)