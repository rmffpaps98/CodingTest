def solution(num_list):
    odd = [str(i) for i in num_list if i % 2 == 1]
    even = [str(i) for i in num_list if i % 2 == 0]
    return int(''.join(odd)) + int(''.join(even))