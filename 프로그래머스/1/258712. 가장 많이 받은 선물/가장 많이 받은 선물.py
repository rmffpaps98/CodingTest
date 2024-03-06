def solution(friends, gifts):
    answer = [0 for _ in range(len(friends))]
    k = len(friends)
    
    gt = [[0] * k for _ in range(k)]
    gp = {i : 0 for i in friends}
    for i in gifts :
        send, receive = i.split()
        gp[send] += 1
        gp[receive] -= 1
        gt[friends.index(send)][friends.index(receive)] += 1
        gt[friends.index(receive)][friends.index(send)] -= 1
        
    for idx, i in enumerate(gt) :
        for ind, j in enumerate(i) :
            if j > 0 :
                answer[idx] += 1
            if j == 0 and idx != ind:
                a = gp[friends[idx]]
                b = gp[friends[ind]]
                if a > b :
                    answer[idx] += 1
        
    return max(answer)