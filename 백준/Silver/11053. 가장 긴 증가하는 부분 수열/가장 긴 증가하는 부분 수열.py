import sys
from operator import index

num = int(sys.stdin.readline().strip())
lists = list(map(int, sys.stdin.readline().strip().split()))

def binary_search(lists, target):
    left, right = 0, len(lists) - 1

    while left <= right:
        mid = (left + right) // 2

        if lists[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

lis = [lists[0]]

for i in range(1, len(lists)):
    if lists[i] > lis[-1]:
        lis.append(lists[i])
    else:
        index = binary_search(lis, lists[i])
        lis[index] = lists[i]

print(len(lis))