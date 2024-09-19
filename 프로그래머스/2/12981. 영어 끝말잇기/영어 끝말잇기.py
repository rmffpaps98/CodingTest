def solution(n, words):
    used = [words[0]]
    last = words[0][-1]
    
    for idx, word in enumerate(words[1:], start=1):
        if word in used or word[0] != last:
            player = (idx % n) + 1
            turn = (idx // n) + 1
            return [player, turn]
        
        used.append(word)
        last = word[-1]
    
    return [0, 0]

