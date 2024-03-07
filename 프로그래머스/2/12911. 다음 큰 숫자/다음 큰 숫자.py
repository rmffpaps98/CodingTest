def solution(n):
    answer = 0
    x = n
    while True :
        x += 1
        if bin(n)[2:].count("1") == bin(x)[2:].count("1") :
            return x
    return answer