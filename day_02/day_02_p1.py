import aoc_tools 

with open('input.txt') as f:
    input = f.read()

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
