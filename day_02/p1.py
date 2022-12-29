from aoc_tools import get_input_string

input = get_input_string(__file__)

data = [[d.split()[0], int(d.split()[1])] for d in input.splitlines()]

horizontal = []
depth = []

for move in data:
    if move[0] == 'forward':
        horizontal.append(move[1])
    if move[0] == 'down':
        depth.append(-move[1])
    if move[0] == 'up':
        depth.append(move[1])

print(abs(sum(depth)) * abs(sum(horizontal)))
