def solution(arr, queries):
    answer = []
    for s, e, k in queries :
        a = arr[s:e+1]
        a.sort()
        for i in a :
            if i > k :
                answer.append(i)
                break
            elif i==a[-1] :
                answer.append(-1)
    return answer