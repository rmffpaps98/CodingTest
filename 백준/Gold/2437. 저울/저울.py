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


##################################################
# 최초 풀이 답안 : 시간복잡도가 높아 비효율적
# n = int(input())

# weight = list(map(int, input().split()))
# weight.sort(reverse=True)

# answer = 0

# for i in range(1, sum(weight)+1) :
#     num = i
#     for j in weight :
#         if num >= j :
#             num -= j
    
#     if num > 0 :
#         answer = i
#         break

# print(answer)
##################################################
