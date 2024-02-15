def solution(sides):
    return 1 if max(sides) < sum(sorted(sides)[:2]) else 2