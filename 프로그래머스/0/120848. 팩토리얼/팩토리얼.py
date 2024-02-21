def solution(n):
    tmp = 1
    for i in range(1, 11) :
        tmp = tmp * i
        if tmp == n :
            return i
        elif tmp > n :
            return i-1