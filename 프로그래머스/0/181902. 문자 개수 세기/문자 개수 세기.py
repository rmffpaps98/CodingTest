def solution(my_string):
    answer = []
    s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s2 = "abcdefghijklmnopqrstuvwxyz"
    for i in s1 :
        answer.append(my_string.count(i))
    for i in s2 :
        answer.append(my_string.count(i))
    return answer