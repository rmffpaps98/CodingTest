def solution(n):
    answer = []
    for i in range(1000) :
        answer.append(n)
        if n % 2 == 0:
            n //= 2
        elif n % 2 == 1:
            n = 3 * n + 1
        
        if n == 1 :
            answer.append(n)
            break
        else : continue
    return answer