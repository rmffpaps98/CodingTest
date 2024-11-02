s = input()

alp = {chr(i): 0 for i in range(97, 123)}

for i in s:
    alp[i] = alp.get(i) + 1

for i in alp.values():
    print(i, end=' ')