import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input().strip())
in_q = []
out_q = []
out_results = []

for _ in range(n):
    com = input().split()

    if com[0] == 'push':
        in_q.append(com[1])
    elif com[0] == 'pop':
        if not out_q:
            while in_q:
                out_q.append(in_q.pop())
        if out_q:
            out_results.append(out_q.pop() + '\n')
        else:
            out_results.append('-1\n')
    elif com[0] == 'size':
        out_results.append(str(len(in_q) + len(out_q)) + '\n')
    elif com[0] == 'empty':
        out_results.append('0\n' if (in_q or out_q) else '1\n')
    elif com[0] == 'front':
        if out_q:
            out_results.append(out_q[-1] + '\n')
        elif in_q:
            out_results.append(in_q[0] + '\n')
        else:
            out_results.append('-1\n')
    elif com[0] == 'back':
        if in_q:
            out_results.append(in_q[-1] + '\n')
        elif out_q:
            out_results.append(out_q[0] + '\n')
        else:
            out_results.append('-1\n')

output(''.join(out_results))