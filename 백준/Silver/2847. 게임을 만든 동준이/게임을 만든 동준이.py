n = int(input())
levels = [int(input()) for _ in range(n)]

score = levels[-1]
cnt = 0

for i in levels[-2::-1]:
    num = i
    while num >= score :
        cnt += 1
        num -= 1
    score = num

print(cnt)