def solution(prices):
    answer = []
    stack = []
    
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] > p:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
        answer.append(0)
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1
    return answer

        
