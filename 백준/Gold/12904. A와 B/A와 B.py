import sys

input_data = sys.stdin.read().splitlines()

S = input_data[0]
T = list(input_data[1]) 

while len(T) > len(S):
    if T[-1] == 'A':
        T.pop() 
    elif T[-1] == 'B':
        T.pop() 
        T.reverse() 
    else:
        break

if "".join(T) == S:
    print(1)
else:
    print(0)