import sys, heapq

input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort()

end_time = []
heapq.heappush(end_time, meetings[0][1])

for i in range(1, n) :
    if meetings[i][0] >= end_time[0] :
        heapq.heappop(end_time)
    heapq.heappush(end_time, meetings[i][1])
        
print(len(end_time))