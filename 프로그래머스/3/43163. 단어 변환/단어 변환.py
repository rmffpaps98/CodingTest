def solution(begin, target, words):
    stack = [(begin, 0)]
    
    if target not in words :
        return 0
    
    while stack:
        word, count = stack.pop()
        
        if word == target:
            return count
        
        for w in words[:]:
            diff = sum(1 for a, b in zip(word, w) if a != b)
            if diff == 1:
                stack.append((w, count + 1))
                words.remove(w)
                break
                
        diff = sum(1 for a, b in zip(word, target) if a != b)
        if diff == 1:
            return count+1
    
    return 0