def solution(numbers, direction):
    return [numbers[1:] + numbers[:1] if direction == 'left' else numbers[-1:] + numbers[:-1]].pop()