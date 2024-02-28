def solution(food):
    answer = ''
    fn = [str(idx)*i for idx, i in enumerate(food)]
    
    for idx, i in enumerate(fn[1:]) :
        answer += str((idx+1)) * (len(i) // 2)
    
    return answer + str(0) + ''.join(sorted(answer, reverse=True))