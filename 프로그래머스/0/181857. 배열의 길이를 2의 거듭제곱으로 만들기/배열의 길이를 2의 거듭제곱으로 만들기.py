def solution(arr):
    cnt = 0
    while True :
        if len(arr) == 2 ** cnt :
            return arr
        else :
            if len(arr) < 2 ** cnt :
                arr.append(0)
            else :
                cnt += 1