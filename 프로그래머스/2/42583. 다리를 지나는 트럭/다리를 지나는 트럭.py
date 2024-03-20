from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    b = deque([0] * bridge_length)
    tw = deque(truck_weights)
    
    w = 0
    while tw:
        answer += 1
        w -= b.popleft()

        if w + tw[0] <= weight:
            w += tw[0]
            b.append(tw.popleft())

        else: 
            b.append(0)
            
    answer += bridge_length
    
    return answer