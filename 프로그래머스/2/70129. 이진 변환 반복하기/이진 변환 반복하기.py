def solution(s):
    answer = []
    z_cnt = 0
    cnt = 0
    
    while True :
        z_cnt += s.count("0")
        
        s = s.replace("0", "")
        c = len(s)
        
        s = format(c, 'b') 
        cnt += 1
        
        if len(s)  == 1 :
            return [cnt, z_cnt]