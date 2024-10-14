def solution(maps):
    stack = [(0, 0, 1)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while stack :
        x, y, d = stack.pop(0)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if ny < 0 or nx < 0 or ny >= len(maps) or nx >= len(maps[0]):
                continue
            else :
                if maps[ny][nx] == 1 or maps[ny][nx] > d+1 :
                    maps[ny][nx] = d+1
                    if ny == len(maps)-1 and nx == len(maps[0])-1 :
                        return d+1
                    stack.append((nx, ny, d+1))
            
    return -1
