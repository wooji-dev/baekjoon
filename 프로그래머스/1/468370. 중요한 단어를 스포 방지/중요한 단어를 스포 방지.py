from collections import deque

def solution(message, spoiler_ranges):
    words = message.split()
    positions = []
    s = 0
    for w in words:
        idx = message.index(w, s)
        positions.append((w, idx, idx + len(w) - 1))
        s = idx + len(w)
    
    messages = deque(positions)
    im_word = []
    im_word_set = set()
    visited = {}
    for w, _, _ in messages:
        visited[w] = visited.get(w, 0)
    
    while messages:
        cur, start, end = messages.popleft()
        is_spoiler = False
        for i in spoiler_ranges:
            if not (end < i[0] or start > i[1]):
                if cur not in im_word_set:
                    im_word.append(cur)
                    im_word_set.add(cur)
                is_spoiler = True
        
        if is_spoiler:
            visited[cur] = visited.get(cur) - 1
        visited[cur] = visited.get(cur) + 1
    
    answer = len(im_word)
    for i in im_word:
        if visited[i] > 0:
            answer -= 1
    return answer