answer = 0

def dfs(k, cnt, d, v) :
    global answer
    if cnt > answer :
        answer = cnt
        
    for i in range(len(d)) :
        if not v[i] and k >= d[i][0] :
            v[i] = True
            dfs(k - d[i][1], cnt+1, d, v)
            v[i] = False
            
def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer