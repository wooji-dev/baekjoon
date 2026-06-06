def solution(numbers, target):
    answer = 0
    
    def dfs(idx, cur_num):
        nonlocal answer
        if idx == len(numbers) and cur_num == target:
            answer += 1
            return
        
        elif idx == len(numbers) and cur_num != target:
            return
        
        dfs(idx+1, cur_num + numbers[idx])
        dfs(idx+1, cur_num - numbers[idx])
        
    dfs(0,0)
    return answer