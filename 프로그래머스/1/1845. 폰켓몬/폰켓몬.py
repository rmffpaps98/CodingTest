def solution(nums):
    p = len(set(nums))

    if len(nums) / 2 > p:
        return p
    else:
        return len(nums) / 2