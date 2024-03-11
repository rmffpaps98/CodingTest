def solution(numbers, target):
    stack = [(0, 0)]
    answer = 0
    n = len(numbers)
    
    while stack:
        idx, value = stack.pop()
        
        if idx == n:
            if value == target:
                answer += 1
            continue

        stack.append((idx + 1, value + numbers[idx]))
        stack.append((idx + 1, value - numbers[idx]))
    
    return answer