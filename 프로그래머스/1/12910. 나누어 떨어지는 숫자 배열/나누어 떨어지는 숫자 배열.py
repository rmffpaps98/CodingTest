def solution(arr, divisor):
    answer = []
    for i in sorted(arr) :
        if i % divisor == 0 :
            answer.append(i)
    return answer if answer else [-1]