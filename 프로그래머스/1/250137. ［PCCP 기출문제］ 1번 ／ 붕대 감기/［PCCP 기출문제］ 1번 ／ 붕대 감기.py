def solution(bandage, health, attacks):
    t, x, y = bandage
    end_time = attacks[-1][0]
    attacks = {attack[0]:attack[1] for attack in attacks}
    combo = 0
    ch = health
    
    for i in range(end_time + 1):
        if i in attacks:
            combo = 0
            ch -= attacks[i]
            
            if ch <= 0:
                return -1
            continue

        combo += 1
        ch += x
        
        if combo == t:
            ch += y
            combo = 0
            
        ch = min(ch, health)
    
    return ch