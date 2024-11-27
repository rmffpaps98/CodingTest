import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))

def cal(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i+1])
    return total

max_val = 0
for i in permutations(a):
    max_val = max(max_val, cal(i))
    
print(max_val)