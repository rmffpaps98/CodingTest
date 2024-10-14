def dfs (node, visited, computers, n) :
    visited[node] = True
    for con in range(n) :
        if con != node and computers[node][con] == 1 and not visited[con] :
            dfs(con, visited, computers, n)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n) :
        if not visited[i] :
            dfs(i, visited, computers, n)
            answer += 1
            
    return answer