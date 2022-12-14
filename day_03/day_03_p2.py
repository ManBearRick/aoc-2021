#Advent of Code 2021 day 3
import collections
from aoc_tools import get_list_data, get_dir_path


input = get_list_data(__file__)
# with open('day_03/example.txt', 'r') as f:
#     input = f.read().splitlines()

counts = collections.defaultdict(int)
for line in input:
    for i , c in enumerate(line):
        if c == '1':
            counts[i] += 1

data_1 = input
index = 0
while len(data_1) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for character_idx in range(0, len(data_1)):
        if data_1[character_idx][index] == '0':
            zero += 1
            zeroes.append(data_1[character_idx])
        else:
            one += 1
            ones.append(data_1[character_idx])      
    if zero > one:
        data_1 = zeroes
    else:
        data_1 = ones
    index += 1
oxygen = int(data_1[0], 2)
print('oxygen is: ', oxygen)

data_2 = input
index = 0
while len(data_2) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for character_idx in range(0, len(data_2)):
        if data_2[character_idx][index] == '0':
            zero += 1
            zeroes.append(data_2[character_idx])
        else:
            one += 1
            ones.append(data_2[character_idx])   
    if one < zero:
        data_2 = ones
    else:
        data_2 = zeroes
    index += 1
co2 = int(data_2[0], 2)
print('CO2 is: ', co2)

print(f"answer is {oxygen * co2}")

