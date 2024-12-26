s = input().title()
cnt = 0

for i in s:
    if i.isupper():
        cnt += 1

print(cnt)