n = int(input())
k = []

for _ in range(n) :
    k.append(int(input()))

w = []
k.sort(reverse=True)

for i in range(1, n+1) :
    w.append(k[0] * i)
    k.pop(0)

print(max(w))