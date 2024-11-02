import sys
from collections import deque
output = sys.stdout.write

n = int(input())
deque = deque()
results = []

for _ in range(n):
    com = sys.stdin.readline().split()

    if com[0] == 'push_front':
        deque.appendleft(int(com[1]))
    elif com[0] == 'push_back':
        deque.append(int(com[1]))
    elif com[0] == 'pop_front':
        if deque:
            results.append(str(deque.popleft()) + '\n')
        else:
            results.append('-1\n')
    elif com[0] == 'pop_back':
        if deque:
            results.append(str(deque.pop()) + '\n')
        else:
            results.append('-1\n')
    elif com[0] == 'size':
        results.append(str(len(deque)) + '\n')
    elif com[0] == 'empty':
        results.append('0\n' if deque else '1\n')
    elif com[0] == 'front':
        if deque:
            results.append(str(deque[0]) + '\n')
        else:
            results.append('-1\n')
    elif com[0] == 'back':
        if deque:
            results.append(str(deque[-1]) + '\n')
        else:
            results.append('-1\n')

output(''.join(results))