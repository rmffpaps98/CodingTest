import sys
input = sys.stdin.readline

n = int(input())
num = sorted([int(input()) for _ in range(n)])

print(round(sum(num) / n))
print(num[n // 2])

freq_dict = {}
max_freq = 0
for x in num:
    freq_dict[x] = freq_dict.get(x, 0) + 1
    max_freq = max(max_freq, freq_dict[x])

mode_list = [key for key, value in freq_dict.items() if value == max_freq]

mode_list.sort()
print(mode_list[1] if len(mode_list) > 1 else mode_list[0])

print(max(num) - min(num))