from aoc_tools import get_input_string

input = get_input_string(__file__)

data = [[d.split()[0], int(d.split()[1])] for d in input.splitlines()]

horizontal = []
depth = 0
aim = 0

for move in data:
    if move[0] == 'up':
        aim += move[1]
    if move[0] == 'down':
        aim += -move[1]
    if move[0] == 'forward':
        horizontal.append(move[1])
        depth += aim * move[1]
print(abs(sum(horizontal)) * abs(depth))