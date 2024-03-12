def solution(word):
    answer = 0
    w = ['A', 'E', 'I', 'O', 'U']
    idx = 0
    
    for i in range(len(w)) :
        idx += 1
        if w[i] == word :
            return idx
        for j in range(len(w)) :
            idx += 1
            if w[i]+w[j] == word :
                return idx
            for k in range(len(w)) :
                idx += 1
                if w[i]+w[j]+w[k] == word :
                    return idx
                for l in range(len(w)) :
                    idx += 1
                    if w[i]+w[j]+w[k]+w[l] == word :
                        return idx
                    for m in range(len(w)) :
                        idx += 1
                        if w[i]+w[j]+w[k]+w[l]+w[m] == word :
                            return idx

    return answer