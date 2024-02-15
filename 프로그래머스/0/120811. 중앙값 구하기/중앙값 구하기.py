def solution(array):
    return sorted(array)[len(array)//2:len(array)//2+1].pop()