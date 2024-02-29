def solution(lottos, win_nums):
    answer = []
    zcnt = 0
    cnt = 0
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for i in lottos :
        if i in win_nums :
            cnt += 1
        if i == 0 :
            zcnt += 1
            
    return [rank[cnt+zcnt], rank[cnt]]