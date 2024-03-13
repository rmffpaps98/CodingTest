def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        idx = 0
        flag = True
        
        for j in i:
            if j in skill:
                if j != skill[idx]:
                    flag = False
                    break
                else:
                    idx += 1
        
        if flag:
            answer += 1
    
    return answer