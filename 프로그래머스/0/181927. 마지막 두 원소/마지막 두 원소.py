def solution(num_list):
    answer = num_list[::-1]
    if answer[0] > answer[1] :
        num_list.append(answer[0] - answer[1])
    else :
        num_list.append(2*answer[0])
    return num_list