def solution(n, words):
    used = []
    p = 0
    cnt = 0
    fail = True

    for idx, i in enumerate(words) :
        fail = False
        p = (idx % n) + 1
        cnt = (idx + n) // n
        if not used :
            used.append(i)
        elif used and used[-1][-1] == i[0] and i not in used  :
            used.append(i)
        elif i in used :
            fail = True
            break
        else :
            fail = True
            break

    return [p, cnt] if fail else [0, 0]