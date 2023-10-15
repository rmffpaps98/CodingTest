from collections import Counter

name = list(input())
name.sort()
counter = Counter(name)

odd = 0
center = ''
answer = ''

for i in counter :
    if counter[i] % 2 != 0 :
        odd += 1
        center += i
    
    for _ in range(counter[i]//2) :
        answer += i

if odd > 1 :
    print("I'm Sorry Hansoo")
elif odd == 0 :
    print(answer + answer[::-1])
else :
    print(answer + center + answer[::-1])