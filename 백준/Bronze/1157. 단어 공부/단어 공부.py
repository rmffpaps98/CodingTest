s = input().upper()
ss = list(set(s))
cnt = []

for i in ss:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(ss[cnt.index(max(cnt))])