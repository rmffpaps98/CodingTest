def solution(a, b, n):
    answer = 0
    
    while n >= a :
        coke, empty = divmod(n, a)
        n = (coke * b) + empty
        answer += coke * b
        
    return answer