def solution(numbers, hand):
    answer = ''
    kp = [[1,4,7], [2,5,8,0], [3,6,9]]
    L, R = [0,3], [2,3]
    
    for i in numbers :
        if i in [1, 4, 7] :
            answer += "L"
            L = [0, kp[0].index(i)]
        elif i in [3, 6, 9] :
            answer += "R"
            R = [2, kp[2].index(i)]
        else :
            s1 = abs(L[0] - 1) + abs(L[1] - kp[1].index(i))
            s2 = abs(R[0] - 1) + abs(R[1] - kp[1].index(i))
            if s1 > s2 :
                answer += "R"
                R = [1, kp[1].index(i)]
            elif s1 < s2 :
                answer += "L"
                L = [1, kp[1].index(i)]
            else :
                if hand == "right" :
                    answer += "R"
                    R = [1, kp[1].index(i)]
                else :
                    answer += "L"
                    L = [1, kp[1].index(i)]
        
    return answer