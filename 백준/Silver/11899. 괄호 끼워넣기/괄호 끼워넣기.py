import sys
input = list(sys.stdin.readline().strip())

# input = [')','(','(',')','(','(',')',')',')']

dic = {'(':0, ')':0}
answer = {'(':0, ')':0}

for i in range(len(input)):
	if input[i] == ')':
		if dic['('] > 0:
			dic['('] -= 1
		else:
			answer['('] += 1
	else:
		dic['('] += 1

answer[')'] = dic['(']



print(answer['('] + answer[')'])