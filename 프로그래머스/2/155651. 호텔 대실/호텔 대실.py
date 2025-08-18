def solution(book_time):
    t = [0] * (1441)
    
    for s, e in book_time:
        sh, sm = s.split(":")
        eh, em = e.split(":")
        st = int(sh) * 60 + int(sm)
        et = int(eh) * 60 + int(em)
        ee = min(et + 10, 1440)
        
        t[st] += 1
        t[ee] -= 1
        
    cur, ans = 0, 0
    for i in range(1440):
        cur += t[i]
        ans = max(ans, cur)
        
    return ans