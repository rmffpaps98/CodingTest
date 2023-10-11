import sys

input = sys.stdin.readline

n, m = map(int, input().split())
package = []
single = []

for _ in range(m):
    p, s = map(int, input().split())
    package.append(p)
    single.append(s)

result = 0

while n > 0:
    min_package = min(package)
    
    if n >= 6:
        min_single = min(single)*6
        n -= 6
    else:
        min_single = min(single)*n
        n -= n
    if min_single < min_package:
        result += min_single
    else:
        result += min_package

print(result)