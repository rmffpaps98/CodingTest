def solution(num, total):
    d = sum(range(num))
    s = (total-d) // num
    return [i for i in range(s, s + num)]
    