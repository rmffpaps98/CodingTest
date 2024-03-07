def solution(arr):
    answer = 0
    arr.sort()
    
    for i in range(len(arr)-1):
        a, b = arr[i], arr[i+1]
        while a != 0:
            tmp = b % a
            a, b = tmp, a
        arr[i+1] = arr[i] * arr[i+1] // b
        
    return arr[i+1]