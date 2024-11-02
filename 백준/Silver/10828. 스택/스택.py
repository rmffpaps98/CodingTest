import sys
output = sys.stdout.write

n = int(input())
stack = []
results = []

for _ in range(n):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        stack.append(com[1])
    elif com[0] == 'pop':
        if stack:
            results.append(stack.pop() + '\n')
        else:
            results.append('-1\n')
    elif com[0] == 'size':
        results.append(str(len(stack)) + '\n')
    elif com[0] == 'empty':
        results.append('0\n' if stack else '1\n')
    else:
        if stack:
            results.append(stack[-1] + '\n')
        else:
            results.append('-1\n')

output(''.join(results))