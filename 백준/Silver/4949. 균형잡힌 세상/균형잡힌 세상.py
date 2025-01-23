import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break

    stack = []
    is_balanced = True

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_balanced = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_balanced = False
                break

    if is_balanced and not stack:
        print("yes")
    else:
        print("no")