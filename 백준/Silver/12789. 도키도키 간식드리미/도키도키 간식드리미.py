from collections import deque

n = int(input())
arr1 = deque(map(int, input().split()))
stack = []
current = 1

while arr1 or stack:
    if arr1 and arr1[0] == current:
        arr1.popleft()
        current += 1
    elif stack and stack[-1] == current:
        stack.pop()
        current += 1
    elif arr1:
        stack.append(arr1.popleft())
    else:
        break

if not stack and not arr1:
    print("Nice")
else:
    print("Sad")