def solution(numer1, denom1, numer2, denom2):
    n = numer1 * denom2 + numer2 * denom1
    d = denom1 * denom2
    for i in range(2, d+1) :
        while n % i == 0 and d % i == 0 :
            n //= i
            d //= i
    return [n, d]