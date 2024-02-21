def solution(i, j, k):
    return sum([list(map(int, str(num))).count(k) for num in range(i, j+1)])