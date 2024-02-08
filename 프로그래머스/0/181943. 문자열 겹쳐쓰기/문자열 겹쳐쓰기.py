def solution(my_string, overwrite_string, s):
    answer = ''
    overlen = len(overwrite_string)
    first = my_string[:s]
    last = my_string[overlen+s:]
    answer = first + overwrite_string + last
    return answer