def solution(phone_book):
    answer = True
    h = {i : 1 for i in phone_book}
        
    for i in phone_book:
        tmp = ""
        for j in i:
            tmp += j
            if tmp in h and tmp != i:
                answer = False
    return answer