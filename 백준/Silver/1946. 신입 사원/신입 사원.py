import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cnt = 1
    N = int(input())
    score = [tuple(map(int, input().split())) for _ in range(N)]
    score.sort()

    standard = score[0][1]

    for i in range(1, N) :
        if standard > score[i][1] :
            cnt += 1
            standard = score[i][1]

    print(cnt)