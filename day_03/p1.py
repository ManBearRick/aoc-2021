#Advent of Code 2021 day 3

from aoc_tools import get_list_data
import collections

# with open('day_03/example.txt', 'r') as f:
#     input = f.read().splitlines()

input = get_list_data(__file__)
print(input)

counts: dict[int, int] = collections.defaultdict(int)
for item in input:
    for i, c in enumerate(item):
        if c == '1':
            counts[i] += 1

gamma = []
epsilon = []

for i in range(len(input[0])):
    if counts[i] > len(input) / 2:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

gamma_int = int(''.join(gamma), 2)
epsilon_int = int(''.join(epsilon), 2)

print('power consumption = ', gamma_int * epsilon_int)






