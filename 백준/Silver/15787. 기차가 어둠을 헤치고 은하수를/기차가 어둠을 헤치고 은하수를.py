import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

train_count = int(input_data[0])
order_num = int(input_data[1])

trains = [[0] * 20 for _ in range(train_count + 1)]

ptr = 2
for _ in range(order_num):
    cmd_type = int(input_data[ptr])
    t_idx = int(input_data[ptr + 1])
    
    if cmd_type == 1:
        seat = int(input_data[ptr + 2])
        trains[t_idx][seat-1] = 1
        ptr += 3
    elif cmd_type == 2:
        seat = int(input_data[ptr + 2])
        trains[t_idx][seat-1] = 0
        ptr += 3
    elif cmd_type == 3:
        for i in range(19, 0, -1):
            trains[t_idx][i] = trains[t_idx][i-1]
        trains[t_idx][0] = 0
        ptr += 2
    elif cmd_type == 4:
        for i in range(0, 19):
            trains[t_idx][i] = trains[t_idx][i+1]
        trains[t_idx][19] = 0
        ptr += 2


result_set = set()
for i in range(1, train_count + 1):
    result_set.add(tuple(trains[i]))

print(len(result_set))