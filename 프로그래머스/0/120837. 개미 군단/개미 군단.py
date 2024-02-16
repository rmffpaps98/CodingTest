def solution(hp):
    count = 0
    for i in [5, 3, 1] :
        if hp > 0 :
            count += hp // i
            hp = hp % i
        if hp == 0 :
            return count