def dfs(node, graph, visited):
    visited[node] = True
    count = 1

    for next_node in graph[node]:
        if not visited[next_node]:
            count += dfs(next_node, graph, visited)

    return count

def solution(n, wires):
    answer = float("inf")
    graph = [[] for _ in range(n + 1)]
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    for s, e in wires:
        visited = [False] * (n + 1)
        
        graph[s].remove(e)
        graph[e].remove(s)
        
        res = dfs(s, graph, visited)
        
        other = n - res
        diff = abs(res - other)
        answer = min(answer, diff)
        
        graph[s].append(e)
        graph[e].append(s)

    return answer
