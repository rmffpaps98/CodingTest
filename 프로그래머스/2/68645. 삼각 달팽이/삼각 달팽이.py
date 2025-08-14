def solution(n):
    tri = [[0]*(i+1) for i in range(n)]
    cnt = 0
    m = (n * (n + 1)) // 2
    r, c = -1, 0
    
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    d = 0
    
    while cnt < m:
        nr = r + dr[d]
        nc = c + dc[d]
        
        in_range = (0 <= nr < n) and (0 <= nc <= nr)
        empty = in_range and (tri[nr][nc] == 0)
        
        if empty:
            r, c = nr, nc
            cnt += 1
            tri[r][c] = cnt 
        elif not empty:
            d = (d + 1) % 3
            
    return [x for row in tri for x in row]
        
        
        