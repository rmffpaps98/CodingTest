def solution(num, k):
    for i in str(num) :
        if int(i) == k :
            return str(num).index(i)+1
    
    return -1