import sys

test = int(sys.stdin.readline())

def hire(people):
    p = []

    for i in range(people):
        man = list(map(int, sys.stdin.readline().split()))
        if(man[0]==people and man[1]==people):
            continue
        else:
            p.append(man)

    p.sort()
    flag = 1

    while flag < len(p):
        if p[flag-1][1] < p[flag][1]:
            p.pop(flag)
            flag = 1
        else:
            flag += 1

    return len(p)

for _ in range(test):
    people = int(sys.stdin.readline())
    print(hire(people))
