def dfs(k, cnt, d, v, answer):
    answer = max(answer, cnt)
    
    for i in range(len(d)):
        if not v[i] and k >= d[i][0]:
            v[i] = True
            answer = dfs(k - d[i][1], cnt + 1, d, v, answer)
            v[i] = False
    
    return answer

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return dfs(k, 0, dungeons, visited, 0)
