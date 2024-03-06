def solution(today, terms, privacies):
    answer = []
    y, m, d = list(map(int, today.split('.')))
    today = y * 336 + m * 28 + d
    terms = {v[0]: int(v[2:]) * 28 for v in terms}
    
    for idx, i in enumerate(privacies) :
        date, t = i.split()
        yr, mt, dy = list(map(int, date.split('.')))
        day = yr * 336 + mt * 28 + dy + terms[t]
        
        if today >= day :
            answer.append(idx+1)
            
    return answer