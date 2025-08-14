from collections import deque

def solution(queue1, queue2):
    answer = 0
    cnt = 0
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    t = s1 + s2
    N = len(q1) + len(q2)
    
    if t % 2 != 0 or max(q1) > (t // 2) or max(q2) > (t // 2):
        return -1
    
    while s1 != s2:
        cnt += 1
        
        if cnt > N + 2:
            return -1
        
        if s1 > s2:
            n = q1.popleft()
            q2.append(n)
            s1, s2 = s1 - n, s2 + n
        elif s1 < s2:
            n = q2.popleft()
            q1.append(n)
            s1, s2 = s1 + n, s2 - n
            
        answer += 1
            
    return answer