def solution(my_string, m, c):
    return ''.join([my_string[i:i+m][c-1:c] for i in range(0, len(my_string), m)])