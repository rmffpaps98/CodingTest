def solution(n):
    n = ((n**0.5) + 1) ** 2
    return n if int(n) == n else -1