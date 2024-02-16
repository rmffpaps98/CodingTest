def solution(arr):
    idx = []
    for i in range(len(arr)) :
        if arr[i] == 2 :
            idx.append(i)
    return arr[min(idx):max(idx)+1] if idx else [-1]