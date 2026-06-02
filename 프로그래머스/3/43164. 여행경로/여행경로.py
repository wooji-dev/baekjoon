def solution(tickets):
    tickets.sort();
    answer = []
    num = len(tickets) 
    used = [False] * num
    
    def dfs(ticket, idx):
        answer.append(ticket[1])
        used[idx] = True
        
        if len(answer) == (num + 1):
            return True
        
        for i in range(num):
            if used[i] == False and tickets[i][0] == ticket[1]:
                # used[i] = True
                if dfs(tickets[i], i):
                    return True
                # used[i] = False
                
        used[idx] = False
        answer.pop()
        return False
    
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            answer = ["ICN"]
            if dfs(tickets[i], i):
                break
    
    return answer