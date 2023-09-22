n = int(input())
n_time = list(map(int, input().split()))

n_time = sorted(n_time)

time_sum = 0
plus_time = 0
for i in n_time :
    plus_time += i
    time_sum += plus_time
    
print(time_sum)