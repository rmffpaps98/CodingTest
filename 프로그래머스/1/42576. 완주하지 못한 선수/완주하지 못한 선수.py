def solution(participant, completion):
    p = dict()
    
    for i in participant:
        p[i] = p.get(i, 0) + 1
    
    for i in completion:
        p[i] -= 1
    
    for key, value in p.items():
        if value == 1:
            return key
