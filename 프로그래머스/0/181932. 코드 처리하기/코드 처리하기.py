def solution(code):
    answer = ''
    mode = False
    for i in range(len(code)) :
        if code[i] == "1" : mode = not mode
        else :
            if not mode :
                if i % 2 == 0 :
                    answer += code[i]
            else :
                if i % 2 == 1 :
                    answer += code[i]
                    
    if not answer : return "EMPTY"
    else : return answer