def solution(data, ext, val_ext, sort_by):
    answer = []
    s = ["code", "date", "maximum", "remain"]
    
    for c, d, m, r in data :
        if ext == s[0] and c < val_ext :
            answer.append([c, d, m, r])
        elif ext == s[1] and d < val_ext :
            answer.append([c, d, m, r])
        elif ext == s[2] and m < val_ext: 
            answer.append([c, d, m, r])
        elif ext == s[3] and r < val_ext :
            answer.append([c, d, m, r])
                
    return sorted(answer, key=lambda x : x[s.index(sort_by)])