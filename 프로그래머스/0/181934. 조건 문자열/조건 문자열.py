def solution(ineq, eq, n, m):
    if eq == "=":
        return int(n <= m) if ineq == "<" else int(n >= m)
    
    return int(n < m) if ineq == "<" else int(n > m)