import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        else:
            l1 = heapq.heappop(scoville)
            l2 = heapq.heappop(scoville)
            new = l1 + (l2 * 2)
            heapq.heappush(scoville, new)
            answer += 1

    if scoville and scoville[0] >= K:
        return answer

    return -1