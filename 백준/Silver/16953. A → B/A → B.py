A, B = map(int, input().split())
cnt = 1

while True : 
    if A == B :
        print(cnt)
        break
    elif A > B or (B % 2 != 0 and B % 10 != 1) :
        print(-1)
        break

    cnt += 1
    if B % 2 == 0 :
        B //= 2
        
    elif B % 2 == 1:
        B //= 10