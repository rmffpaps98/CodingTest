def solution(ingredient):
    answer = 0
    s = ''.join(list(map(str, ingredient)))
    
    while '1231' in s:
        if s.find('1231') >= 4:
            s = s[s.find('1231')-4:]
        s = s.replace('1231','',1)
        answer += 1
    return answer