def solution(array):
    return [[i, idx] for idx, i in enumerate(array) if i == max(array)].pop()