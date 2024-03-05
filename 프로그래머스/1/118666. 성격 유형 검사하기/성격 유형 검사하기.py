def solution(survey, choices):
    answer = ""
    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    
    for i, j in zip(survey,choices):
        if i not in my_dict.keys():
            i = i[::-1]
            my_dict[i] -= j-4
        else:
            my_dict[i] += j-4

    for i in my_dict.keys():
        if my_dict[i] > 0:
            answer += i[1]
        elif my_dict[i] < 0:
            answer += i[0]
        else:
            answer += sorted(i)[0]

    return answer