def dfs(graph, start, path, visited, tickets):
    if len(path) == len(tickets) + 1:
        return path
    
    for idx, (s, d) in enumerate(tickets):
        if s == start and not visited[idx]:
            visited[idx] = 1
            path.append(d)
            result = dfs(graph, d, path, visited, tickets)
            if result:
                return result
            visited[idx] = 0
            path.pop()
    return None

def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    graph = {s:d for s, d in tickets}
    
    path = ['ICN']
    visited = [0] * len(tickets)
    
    return dfs(graph, 'ICN', path, visited, tickets)
