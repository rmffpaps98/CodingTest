N = int(input())
num = [i for i in str(N)]
num.sort(reverse=True)

if int(''.join(num)) % 30 == 0 :
    print(int(''.join(num)))
else :
    print(-1)