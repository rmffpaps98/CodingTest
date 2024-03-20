def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x : (x[0], x*3), reverse=True))))