def solution(s):
    dic = {}
    tmp = ''
    
    for i in s:
        if i.isdigit():
            tmp += i
        else:
            if tmp:
                dic[tmp] = dic.get(tmp, 0) + 1
                tmp = ''
    
    if tmp:
        dic[tmp] = dic.get(tmp, 0) + 1
    
    return [int(num) for num in sorted(dic, key=lambda x: dic[x], reverse=True)]
