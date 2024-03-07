def solution(s):
    cnt = 0
    zero = 0
    
    while len(s) > 1 :
        cnt += 1
        if "0" in s :
            zero += s.count("0")
            s = s.replace("0", "")
        
        s = bin(len(s))[2:]
            
    return [cnt, zero]