def solution(num_list):
    sum_plus = sum(num_list) ** 2
    sum_mul = 1
    for i in num_list :
        sum_mul *= i
    if sum_plus > sum_mul : return 1
    else : return 0