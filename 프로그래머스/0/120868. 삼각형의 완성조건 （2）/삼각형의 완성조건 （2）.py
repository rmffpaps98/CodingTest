def solution(sides):
    sides.sort()
    answer = list(range(sides[1] - sides[0]+1, sides[0] + sides[1]))
    return len(answer)