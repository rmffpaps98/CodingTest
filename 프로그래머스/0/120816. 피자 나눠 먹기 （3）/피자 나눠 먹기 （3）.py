def solution(slice, n):
    answer = 0
    while n > 0 :
        answer += 1
        n -= slice
    return answer