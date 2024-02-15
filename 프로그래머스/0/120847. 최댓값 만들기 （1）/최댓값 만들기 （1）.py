def solution(numbers):
    return sorted(numbers)[-2:][0] * sorted(numbers)[-2:][1]