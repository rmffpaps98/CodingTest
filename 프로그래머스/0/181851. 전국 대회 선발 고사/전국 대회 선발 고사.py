def solution(rank, attendance):
    rk = []
    for i, j in zip(rank, attendance) :
        if j :
            rk.append(i)
    num = []
    for i in sorted(rk)[:3] :
        num.append(rank.index(i))
    return 10000 * num[0] + 100 * num[1] + num[2]