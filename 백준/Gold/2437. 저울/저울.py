n = int(input())
weight = list(map(int, input().split()))
weight.sort()

answer = 1

for w in weight:
    if w <= answer:
        answer += w
    else:
        break

print(answer)