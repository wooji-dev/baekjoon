import sys

rows = int(sys.stdin.readline())

if rows == 1:
    print(3 % 9901)
else:
    prev = [1, 1, 1]
    for row in range(2, rows + 1):
        a, b, c = prev
        prev = [sum(prev), a + b, a + c]
    print(sum(prev) % 9901)