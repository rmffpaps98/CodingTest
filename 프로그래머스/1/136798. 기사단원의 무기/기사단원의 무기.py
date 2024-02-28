def solution(number, limit, power):
    weapon = []
    
    for i in range(1, number + 1):
        d = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                d += 1
                if j != i // j:
                    d += 1
        
        if d > limit:
            weapon.append(power)
        else:
            weapon.append(d)
    
    return sum(weapon)