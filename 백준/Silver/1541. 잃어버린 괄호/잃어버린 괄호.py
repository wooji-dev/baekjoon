import sys

groups = sys.stdin.readline().strip().split('-')

results = []

for group in groups:
    sum_val = sum(map(int, group.split('+')))
    results.append(sum_val)

answer = results[0]
for i in range(1, len(results)):
    answer -= results[i]

print(answer)