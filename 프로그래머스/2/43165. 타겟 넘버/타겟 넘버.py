def dfs(idx, value, numbers, target):
    if idx == len(numbers):
        return 1 if value == target else 0
    
    add = dfs(idx + 1, value + numbers[idx], numbers, target)
    sub = dfs(idx + 1, value - numbers[idx], numbers, target)
    
    # 두 경우의 수를 더한 결과를 반환
    return add + sub

def solution(numbers, target):
    return dfs(0, 0, numbers, target)
