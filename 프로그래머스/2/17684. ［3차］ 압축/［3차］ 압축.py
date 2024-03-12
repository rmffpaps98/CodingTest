def solution(msg):
    answer = []
    a = {j : i+1 for i, j in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    
    while True:
        if msg in a:
            answer.append(a[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in a:
                answer.append(a[msg[0:i-1]])
                a[msg[0:i]] = len(a)+1
                msg = msg[i-1:]
                break

    return answer