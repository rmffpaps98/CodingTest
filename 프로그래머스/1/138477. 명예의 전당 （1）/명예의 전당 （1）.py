def solution(k, score):
    answer = []
    rank_list = []
    
    for i in score :
        rank_list.append(i)
        rank_list = sorted(rank_list, reverse=True)[:k]
        
        answer.append(rank_list[-1])
    return answer