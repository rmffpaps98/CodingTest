x, y = map(int, input().split())

mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(day[(sum(mon[:x-1]) + y) % 7])