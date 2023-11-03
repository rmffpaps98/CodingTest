import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        else:
            lowest = heapq.heappop(scoville)
            second_lowest = heapq.heappop(scoville)
            new_scoville = lowest + (second_lowest * 2)
            heapq.heappush(scoville, new_scoville)
            answer += 1

    if scoville and scoville[0] >= K:
        return answer

    return -1
