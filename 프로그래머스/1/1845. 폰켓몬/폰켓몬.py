def solution(nums):
    c = len(nums) // 2
    nums = set(nums)
    
    return min(c, len(nums))