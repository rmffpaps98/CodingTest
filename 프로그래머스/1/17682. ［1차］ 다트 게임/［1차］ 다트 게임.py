def solution(dartResult):
    num = 0
    scores = []
    
    dartResult = dartResult.replace('10','k')
    dartResult = ['10' if i == 'k' else i for i in dartResult]

    for i in list(dartResult):
        if i.isdigit():
            num = int(i)
        elif i.isalpha():
            if i == 'K' : num = 10
            if i == 'S': num **= 1
            elif i == 'D': num **= 2
            elif i == 'T': num **= 3
            scores.append(num)
            num = 0
        elif i == '*':
            if len(scores) > 1:
                scores[-2] *= 2
            scores[-1] *= 2
        elif i == '#':
            scores[-1] *= -1

    return sum(scores)