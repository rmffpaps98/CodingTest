def solution(a, b):
    ans1 = str(a) + str(b)
    ans2 = 2 * a * b
    return max(int(ans1), ans2)