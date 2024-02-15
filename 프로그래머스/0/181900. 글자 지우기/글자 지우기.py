def solution(my_string, indices):
    for i in sorted(indices, reverse=True) :
        my_string = my_string[:i] + my_string[i+1:]
    return my_string