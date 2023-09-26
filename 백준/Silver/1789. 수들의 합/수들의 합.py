n = int(input())
S = 0
cnt = 0

while True :
    cnt += 1
    S += cnt
    if S > n :
        print(cnt - 1)
        break
    elif S == n :
        print(cnt)
        break