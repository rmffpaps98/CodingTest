def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2) :
        n = []
        for x, y in zip(i, j) :
            n.append(x+y)
        answer.append(n)
    return answer