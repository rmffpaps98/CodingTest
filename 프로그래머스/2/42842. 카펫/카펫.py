def solution(brown, yellow):
    for i in range(1, int(yellow**0.5) + 1) :
        if yellow % i == 0 :
            w = yellow // i
            h = i
            if 2 * (w+h) + 4 == brown :
                return [w+2, h+2]