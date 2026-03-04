import sys

input_data = sys.stdin.read().splitlines()
lines = int(input_data[0])
points = []

for i in range(1, lines+1):
    a, b = map(int, input_data[i].split())
    points.append((a, b))


points.sort()
length = 0
start = points[0][0]
end = points[0][1]

for i in range(1, len(points)):
	current_start, current_end = points[i]
	if current_start <= end:
		end = max(end, current_end)
	else :
		length += end - start
		start = current_start
		end = current_end		

length += end - start



print(length)