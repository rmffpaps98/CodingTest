def solution(bin1, bin2):
    answer = 0
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    answer = bin(bin1+bin2)
    print(answer)
    return answer[2:]