def solution(sequence, k):
    answer = []
    s = 0
    left = 0
    l = float("inf")
    
    for right in range(len(sequence)):
        s += sequence[right]
        
        while s >= k:
            if s == k:
                if l > right - left:
                    l = right - left
                    answer = [left, right]
            
            s -= sequence[left]
            left += 1
            
    return answer