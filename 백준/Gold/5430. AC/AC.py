import sys
from collections import deque


def solution(ops, num_arr):
    is_reversed = False

    for op in ops:
        if op == 'R':
            is_reversed = not is_reversed
        elif op == 'D':
            if not num_arr:
                return 'error'
            if is_reversed:
                num_arr.pop()
            else:
                num_arr.popleft()

    if is_reversed:
        num_arr.reverse()

    return '[' + ','.join(num_arr) + ']'


input_lines = sys.stdin.read().splitlines()
tests = int(input_lines[0])

for i in range(tests):
    base = 1 + i * 3
    ops = input_lines[base]
    # length = int(input_lines[base + 1])  # 사용 안 함
    arr_str = input_lines[base + 2]

    if arr_str == '[]':
        num_arr = deque()
    else:
        num_arr = deque(arr_str[1:-1].split(','))

    print(solution(ops, num_arr))
