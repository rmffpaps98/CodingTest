def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    rdn = {i : 0 for i in id_list}
    
    for i in set(report) :
        _, rd = i.split()
        rdn[rd] += 1
        
    ban = [i for i, j in rdn.items() if j >= k]
    
    for i in set(report) :
        rr, rd = i.split()
        if rd in ban :
            answer[id_list.index(rr)] += 1
            
    return answer