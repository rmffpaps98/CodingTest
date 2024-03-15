def solution(record):
    answer = []
    d = {}
    
    for i in record :
        if 'Enter' in i or 'Change' in i:
            _, ID, name = i.split()
            d[ID] = name
        
    for i in record :
        if 'Enter' in i :
            _, ID, _ = i.split()
            msg = d[ID] + "님이 들어왔습니다."
            answer.append(msg)
        elif 'Leave' in i :
            _, ID = i.split()
            msg = d[ID] + "님이 나갔습니다."
            answer.append(msg)
    
    return answer