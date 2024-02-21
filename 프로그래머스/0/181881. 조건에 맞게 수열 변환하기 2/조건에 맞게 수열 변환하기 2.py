def solution(arr):
    answer = 0
    prev = arr
    while True :
        tmp = []
        for i in prev :
            if i % 2 == 0 and i >= 50 :
                tmp.append(i//2)
            elif i % 2 == 1 and i < 50 :
                tmp.append(i*2 + 1)
            else :
                tmp.append(i)
        
        if prev == tmp : break
        else : prev = tmp
        answer += 1
    return answer