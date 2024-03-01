def solution(keymap, targets):
    answer = []
    kp = {}
    
    for k in keymap:
        for i, s in enumerate(k):
            kp[s] = min(i + 1, kp[s]) if s in kp else i + 1

    for i, t in enumerate(targets):
        c = 0
        for s in t:
            if s not in kp:
                c = - 1
                break
            c += kp[s]
        answer.append(c)

    return answer