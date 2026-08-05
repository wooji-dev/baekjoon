def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = '0' if numbers[0] == '0' else ''.join(numbers)
    
    return answer