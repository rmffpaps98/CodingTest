import sys

input = sys.stdin.readline

n = int(input())
sequnce = [int(input()) for _ in range(n)]

pos = []
neg = []

for i in sequnce :
    if i > 0 :
        pos.append(i)
    else :
        neg.append(i)

pos.sort()
neg.sort(reverse=True)
sum = 0

while len(pos) >= 2 :
    a = pos.pop()
    b = pos.pop()

    if a == 1 or b == 1 :
        sum += a + b 
    else :
        sum += a * b

if pos :
    sum += pos.pop()

while len(neg) >= 2 :
    a = neg.pop()
    b = neg.pop()

    sum += a * b

if neg :
    sum += neg.pop()

print(sum)