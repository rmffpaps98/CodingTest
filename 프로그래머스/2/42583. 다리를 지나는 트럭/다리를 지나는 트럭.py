def solution(bridge_length, weight, truck_weights):
    answer = 0
    b = [0] * bridge_length
    w = 0
    idx = 0

    while idx < len(truck_weights):
        answer += 1
        w -= b.pop(0)

        if w + truck_weights[idx] <= weight:
            w += truck_weights[idx]
            b.append(truck_weights[idx])
            idx += 1
        else:
            b.append(0)

    answer += bridge_length
    
    return answer