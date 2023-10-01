N = int(input())
word = [str(input()) for _ in range(N)]

dic = {}

for i in word :
    p = len(i) - 1
    for j in i :
        if j in dic :
            dic[j] += 10 ** p
        else :
            dic[j] = 10 ** p
        p -= 1

dic = sorted(dic.values(), reverse=True)

answer = 0
s = 9

for i in dic :
    answer += i * s
    s -= 1

print(answer)