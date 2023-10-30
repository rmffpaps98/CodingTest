def solution(msg):
    answer = []
    alphabet = {j : i+1 for i, j in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    idx = 27
    
    msg = list(msg) + ["0"]
    start, end = 0, 1
    
    while end < len(msg):
        while ''.join(msg[start:end]) in alphabet:
            end += 1
            
        alphabet[''.join(msg[start:end])] = idx
        idx += 1
        
        answer.append(alphabet[''.join(msg[start:end-1])])
        
        start, end = end - 1, end
    return answer