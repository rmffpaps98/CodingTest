def solution(numbers):
    answer = []
    stack = []

    for num in reversed(numbers):
        while stack and stack[-1] <= num:
            stack.pop()
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
        stack.append(num)

    return list(reversed(answer))