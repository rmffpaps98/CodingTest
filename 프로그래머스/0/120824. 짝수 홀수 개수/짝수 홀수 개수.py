def solution(num_list):
    o = [i for i in num_list if i % 2 == 1]
    e = [i for i in num_list if i % 2 == 0]
    return [len(e), len(o)]