import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

while len(s) < len(t) :
    if t[-1] == 'A' and len(t) > len(s):
        t = t[:-1]

    if t[-1] == 'B' and len(t) > len(s):
        t = t[:-1]
        t = t[::-1]

if s == t :
    print(1)
else :
    print(0)