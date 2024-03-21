def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for connect in range(n):
                        if connect != node and computers[node][connect] == 1 and not visited[connect]:
                            stack.append(connect)
            answer += 1

    return answer