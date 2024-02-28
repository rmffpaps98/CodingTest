def solution(name, yearning, photo):
    answer = []
    dict_name = dict(zip(name, yearning))
    
    for i in photo:
        score = sum([dict_name.get(char, 0) for char in i])
        answer.append(score)
    
    return answer