def solution(players, callings):
    play = {i : idx for idx, i in enumerate(players)}
    
    for i in callings :
        idx = play[i]
        play[i] -= 1
        play[players[idx-1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
    return players