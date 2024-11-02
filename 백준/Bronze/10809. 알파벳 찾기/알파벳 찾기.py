s = input()

alp = {chr(i): 0 for i in range(97, 123)}

for i in alp.keys():
    if i in s:
        alp[i] = alp.get(i) + s.index(i)
    else:
        alp[i] = -1

for i in alp.values():
    print(i, end=' ')