def solution(arr, idx):
    for i in range(len(arr[idx:])) :
        if arr[idx:][i] == 1:
            return idx + i
    
    return -1