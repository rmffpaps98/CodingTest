def solution(score):
    a = []
    rank = []
    for i in score :
        avg = sum(i) / 2
        a.append(avg)
    sort_avg = sorted(a, reverse=True)
    
    return [sort_avg.index(i)+1 for i in a]