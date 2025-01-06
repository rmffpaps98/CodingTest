n = int(input())

en = 666
cnt = 0

while True:
    if '666' in str(en):
        cnt += 1
        if cnt == n:
            break
    en += 1

print(en)