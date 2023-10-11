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


#####################################################################
# 처음 제출답안  >>  단품 6개 구매가 패키지보다 싼 경우를 포함하지 않음
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cases = []
ones = []

for _ in range(m):
    c, o = map(int, input().split())
    cases.append(c)
    ones.append(o)

result = 0

while n > 0:
    min_case = min(cases)
    min_one = min(ones)
    
    if n >= 6 and min_case <= 6 * min_one:
        result += min_case
        n -= 6
    else:
        result += min(min_case, min_one * n)
        break

print(result)
#####################################################################
