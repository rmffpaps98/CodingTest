import sys
input = sys.stdin.readline

n = int(input())
cod = list(map(int, input().split()))
s_cod = sorted(list(set(cod)))

dict = {i: idx for idx, i in enumerate(s_cod)}

for i in cod:
    print(dict[i], end=' ')