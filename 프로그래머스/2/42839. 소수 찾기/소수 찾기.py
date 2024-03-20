def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def dfs(numbers, nums, stack, visit):
    if stack:
        nums.add(int("".join(stack)))
            
    for i in range(len(numbers)):
        if not visit[i]:
            visit[i] = True
            stack.append(numbers[i])
            dfs(numbers, nums, stack, visit)
            visit[i] = False
            stack.pop()

def solution(numbers):
    answer = 0
    stack = []
    nums = set()
    visit = [False] * len(numbers)
    
    dfs(numbers, nums, stack, visit)
    
    for i in nums :
        if is_prime(i) :
            answer += 1
    
    return answer