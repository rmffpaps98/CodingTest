def solution(n):
    z_cnt = format(n, 'b').count('1')
    while True :
        n += 1
        if z_cnt == format(n, 'b').count('1') :
            return n
        else :
            continue