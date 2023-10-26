import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n == 1 :
  print(1)

elif n == 2 :
  print(min((m + 1) // 2, 4))

elif m < 7 :
    print(min(m, 4))
    
else :
    print(m - 2)