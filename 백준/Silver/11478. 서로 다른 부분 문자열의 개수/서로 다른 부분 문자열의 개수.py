s = input()
ss = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        ss.add(s[i:j+1])

print(len(ss))