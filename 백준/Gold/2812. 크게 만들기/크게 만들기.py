import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = input().rstrip()
stack = []

for num in nums :
    while stack and stack[-1] < num and k > 0 :
        stack.pop()
        k -= 1
    stack.append(num)

print(''.join(stack[:len(stack)-k]))