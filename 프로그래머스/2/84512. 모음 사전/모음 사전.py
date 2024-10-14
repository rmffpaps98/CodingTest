def dfs(current_word, word, w, answer):
    if current_word == word:
        return answer[0]

    if len(current_word) == 5:
        return None

    for vowel in w:
        answer[0] += 1
        result = dfs(current_word + vowel, word, w, answer)
        if result is not None:
            return result

def solution(word):
    w = ['A', 'E', 'I', 'O', 'U']
    answer = [0]
    

    return dfs('', word, w, answer)
