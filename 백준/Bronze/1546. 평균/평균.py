n = int(input())
arr = list(map(int, input().split()))
m = max(arr)

for i in range(len(arr)):
    arr[i] /= m
    arr[i] *= 100

print(sum(arr)/n)