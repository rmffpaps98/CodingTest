def solution(price, money, count):
    answer = 0
    c = 0
    for i in range(count) :
        c += price
        answer += c
    return answer - money if money < answer else 0