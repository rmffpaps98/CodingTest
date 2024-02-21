def solution(array, n):
    array.sort()
    tmp = []
    for i in array :
        tmp.append(abs(i-n))
    
    return array[tmp.index(min(tmp))]