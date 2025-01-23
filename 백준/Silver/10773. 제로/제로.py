import sys
input = sys.stdin.readline

k = int(input())
arr = []

for _ in range(k):
    i = int(input())
    if i != 0:
        arr.append(i)
    else:
        arr.pop()
        
print(sum(arr))