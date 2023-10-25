import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cd = list(map(int, input().split()))
cd.sort()

distance = []
for i, j in zip(cd, cd[1:]) : distance.append(j-i)

distance.sort(reverse=True)

print(sum(distance[k-1:]))