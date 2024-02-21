def solution(balls, share):
    bf = 1
    bs = 1
    sf = 1
    for i in range(1, balls+1) :
        bf *= i
    for i in range(1, balls-share+1) :
        bs *= i
    for i in range(1, share+1) :
        sf *= i
    
    return bf // (bs * sf)