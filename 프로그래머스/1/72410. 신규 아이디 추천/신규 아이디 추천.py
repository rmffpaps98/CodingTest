def solution(new_id):
    answer = ''
    
    for i in new_id :
        if i in '-_.' or i.isalpha() or i.isdigit() :
            answer += i.lower()
    
    while '..' in answer :
        answer = answer.replace('..', '.')
    
    answer = answer.lstrip('.').strip('.')
    
    if not answer : answer += 'a'
    
    if len(answer) >= 16 :
        answer = answer[:15].strip('.')
        
    while len(answer) < 3 :
        answer += answer[-1]
    
    return answer