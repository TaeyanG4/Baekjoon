def solution(ineq, eq, n, m):
    if n >= m and ineq == '>' and eq == '=':
        return 1
    if n <= m and ineq == '<' and eq == '=':
        return 1
    if n > m and ineq == '>' and eq == '!':
        return 1
    if n < m and ineq == '<' and eq == '!':
        return 1    
    return 0