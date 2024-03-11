def solution(str1, str2):
    a1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    a2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    aub = set(a1) | set(a2)
    anb = set(a1) & set(a2)
    
    if len(aub) == 0 :
        return 65536

    a = sum([min(a1.count(i), a2.count(i)) for i in anb])
    b = sum([max(a1.count(i), a2.count(i)) for i in aub])
        
    return int((a/b) * 65536)
        