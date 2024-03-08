def solution(want, number, discount):
    answer = 0
    n = len(discount)
    wn = {i : j for i, j in zip(want, number)}
    for i in range(n - 9) :
        s = discount[i:i+10]
        sn = {i : s.count(i) for i in s}
        if wn == sn :
            answer += 1
    return answer