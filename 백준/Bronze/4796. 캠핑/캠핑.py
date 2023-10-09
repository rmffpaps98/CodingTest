import sys, heapq

input = sys.stdin.readline

i = 1

while True :
    l ,p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0 :
        break
    
    days = (l * (v // p)) + min(v%p, l)
    print("Case {}:".format(i), days)
    i += 1
