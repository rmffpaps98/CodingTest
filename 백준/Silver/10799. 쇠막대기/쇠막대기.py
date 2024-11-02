rb = str(input())
stack = []
cnt = 0

for i in range(len(rb)):
    if rb[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if rb[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)