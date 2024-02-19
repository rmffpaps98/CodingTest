def solution(arr, queries):
    for s, e in queries:
        q = list(range(s, e+1))
        for i in q :
            arr[i] += 1
    return arr