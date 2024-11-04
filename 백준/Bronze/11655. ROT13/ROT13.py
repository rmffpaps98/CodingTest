s = input()
answer = ''

for i in s:
    if i.isalpha():
        if i.islower():
            i = ord(i) + 13
            if i > ord('z'):
                i -= 26
            answer += chr(i)
        elif i.isupper():
            i = ord(i) + 13
            if i > ord('Z'):
                i -= 26
            answer += chr(i)
    else:
        answer += i

print(answer)