def solution(n, k):
    answer = 0
    t = ''
    
    while n > 0:
        t += str(n % k)
        n //= k
    t = ''.join(reversed(t))

    for i in t.split('0'):
        if i == '':
            continue
        for j in range(2,int(int(i) ** (1/2)) + 1):
            if int(i) % j == 0:
                break
        else:
            if i != '1':
                answer += 1
    return answer