def solution(numbers):
    answer = []

    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)
            continue

        nb = '0' + bin(i)[2:]
        nb = nb[:nb.rindex('0')] + '10' + nb[nb.rindex('0') + 2:]
        answer.append(int(nb, 2))

    return answer