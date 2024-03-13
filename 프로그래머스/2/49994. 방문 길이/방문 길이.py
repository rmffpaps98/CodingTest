def solution(dirs):
    stack = set()
    x, y = 0, 0
    d = {"U" : (0, 1), "D" : (0, -1), "R" : (1, 0), "L" : (-1, 0)}
    
    for i in dirs :
        nx, ny = x, y
        dx, dy = d[i]
        if -5 <= x + dx <= 5 and -5 <= y + dy <= 5 :
            x += dx
            y += dy
        if (nx, ny, x, y) not in stack and (nx, ny) != (x, y):
            stack.add((nx, ny, x, y))
            stack.add((x, y, nx, ny))
    
    return len(stack) // 2