n = int(input())
answer = ''

if n == 0:
    print(0)
else:
    while n:
        if n % -2:
            n = (n // -2) + 1
            answer += '1'
        else:
            n //= -2
            answer += '0'

    print(answer[::-1])