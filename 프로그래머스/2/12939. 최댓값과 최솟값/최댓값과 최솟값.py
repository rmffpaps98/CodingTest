def solution(s):
    return "{} {}".format(min(list(map(int, s.split()))), max(list(map(int, s.split()))))