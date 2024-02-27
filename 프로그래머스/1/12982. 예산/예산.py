def solution(d, budget):
    count = 0
    for i in sorted(d) :
        if budget >= i :
            budget -= i
            count += 1
        else :
            break
    return count