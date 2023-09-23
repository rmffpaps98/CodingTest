n = int(input())
meeting = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

prev_end = 0
cnt1 = 0
cnt2 = 0

for meet in sorted(meeting, key=lambda x : x[0]):
    start, end = meet
    if start >= prev_end:
        cnt1 += 1
        prev_end = end

prev_end = 0

for meet in sorted(meeting, key=lambda x : x[1]):
    start, end = meet
    if start >= prev_end:
        cnt2 += 1
        prev_end = end

print(max(cnt1, cnt2))