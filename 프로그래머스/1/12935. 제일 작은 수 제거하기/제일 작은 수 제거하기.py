def solution(arr):
    m = sorted(arr)[0]
    arr.remove(m)
    return arr if arr else [-1]