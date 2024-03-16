def solution(files):
    answer = []
    for i in files:
        head, number, tail = '', '', ''

        for j in range(len(i)):
            if i[j].isdigit():
                number += i[j]
            elif not number:
                head += i[j]
            else:
                tail = i[j:]
                break
        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(i) for i in answer]