import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def cal(a, b):
    if b == 1:
        return a % c
    if b % 2 == 0:
        half = cal(a, b // 2)
        return (half * half) % c
    else:
        return (a * cal(a, b-1)) % c

print(cal(a, b))