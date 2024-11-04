s = input()
s_list = []

for i in range(len(s)):
    s_list.append(s[i:])

for i in sorted(s_list):
    print(i)