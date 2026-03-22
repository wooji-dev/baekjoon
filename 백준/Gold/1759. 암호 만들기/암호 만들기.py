import sys
import itertools

num, chars = map(int, sys.stdin.readline().strip().split())
char_list = list(sys.stdin.readline().strip().split())

char_list.sort()
test= ['a', 'e', 'i', 'o', 'u']

solution = list(itertools.combinations(char_list, num))

for i in solution:
    a = 0
    b = 0
    for j in i:
        if j in test:
            a += 1
        else:
            b += 1

    if a >= 1 and b >= 2:
        print(*i,sep="")