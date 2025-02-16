import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)
output = sys.stdout.write

def cantor(n):
    if n == 0:
        return "-"

    prev = cantor(n - 1)
    space = " " * len(prev)
    return prev + space + prev

for i in input().split():
    output(cantor(int(i)) + "\n")