def solution(my_string, is_prefix):
    pre = [my_string[:i+1] for i in range(len(my_string))]
    if is_prefix in pre : return 1
    else : return 0