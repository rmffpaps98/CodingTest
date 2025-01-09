import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pkm_dict_name = {}
pkm_dict_num = {}

for i in range(1, n+1):
    pkm = input().rstrip()
    pkm_dict_name[pkm] = i
    pkm_dict_num[i] = pkm

for _ in range(m):
    p = input().rstrip()

    if p.isalpha():
        print(pkm_dict_name[p])
    else:
        print(pkm_dict_num[int(p)])