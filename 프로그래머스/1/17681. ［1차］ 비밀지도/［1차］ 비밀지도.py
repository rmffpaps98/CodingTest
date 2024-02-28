def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        comb = bin(i | j)[2:].zfill(n)
        comb = comb.replace('1', '#').replace('0', ' ')
        answer.append(comb)
        
    return answer