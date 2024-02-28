def solution(n, m, section):
    answer = 0
    w = [False] * n

    for i in section:
        w[i-1] = True


    for i in range(n):
        if w[i]:
            answer += 1
            for j in range(i, m+i):
                if len(w) > j :
                    w[j] = False

    return answer