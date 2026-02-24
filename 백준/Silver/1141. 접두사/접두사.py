import sys

num = int(sys.stdin.readline())
words = []
answer = num

for i in range(num):
	word = sys.stdin.readline().strip()
	words.append(word)

# num= 6
# words=["a","ab","abc","abcd","abcde","abcdef"]
# words=["hello","hi","h","run","rerun","running"]

words.sort()

i = 0
while i < len(words) - 1:
	if words[i].startswith(words[i+1]):
		answer = answer - 1
		words.remove(words[i+1])
	elif words[i+1].startswith(words[i]):
		answer = answer - 1
		words.remove(words[i])
	else:
		i += 1


print(len(words))