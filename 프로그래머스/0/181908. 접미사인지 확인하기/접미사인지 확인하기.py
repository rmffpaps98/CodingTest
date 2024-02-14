def solution(my_string, is_suffix):
    if is_suffix in [my_string[i:] for i in range(len(my_string))] : return 1
    else : return 0