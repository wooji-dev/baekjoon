def solution(nums):
    answer = 0
    size = len(nums) // 2
    nums = set(nums)
    
    if len(nums) >= size:
        answer = size
    else:
        answer = len(nums)
    return answer