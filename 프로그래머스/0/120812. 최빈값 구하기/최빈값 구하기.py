def solution(array):
    answer = 0
    m = 0
    for i in set(array) :
        if array.count(i) > m :
            m = array.count(i)
            answer = i
        elif array.count(i) == m :
            answer = -1
    
    return answer