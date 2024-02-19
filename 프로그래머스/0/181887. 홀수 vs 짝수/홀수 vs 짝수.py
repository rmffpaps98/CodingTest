def solution(num_list):
    answer = [0, 0]
    for i in range(len(num_list)) :
        if i % 2 == 0 :
            answer[0] += num_list[i]
        else :
            answer[1] += num_list[i]
    return max(answer)