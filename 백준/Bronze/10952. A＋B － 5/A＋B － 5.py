import sys
input = sys.stdin.readline

while True:
    result = sum(map(int, input().split()))

    if result == 0:
        break
    else:
        print(result)