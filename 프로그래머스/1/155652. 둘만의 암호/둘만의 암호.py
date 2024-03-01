def solution(s, skip, index):
    answer = ''
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip :
        a = a.replace(i, '')
        
    for i in s :
        answer += a[(a.index(i) + index) % len(a)]
        
    return answer