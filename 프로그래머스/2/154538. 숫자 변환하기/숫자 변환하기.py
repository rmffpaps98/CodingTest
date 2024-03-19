from collections import deque

def solution(x, y, n):
    visited = set()
    queue = deque([(x, 0)])
    
    while queue:
        num, count = queue.popleft()

        if num == y:
            return count

        if num in visited:
            continue
        
        visited.add(num)

        if num + n <= y:
            queue.append((num + n, count + 1))
        if num * 2 <= y:
            queue.append((num * 2, count + 1))
        if num * 3 <= y:
            queue.append((num * 3, count + 1))
    
    return -1