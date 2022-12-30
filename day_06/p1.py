#Advent of Code 2021 day 6
import os

_heredir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(_heredir, 'input.txt')

with open(filename, 'r') as f:
    input_str = f.read()

input_str = '3,4,3,1,2'

fish_list = [int(fish) for fish in input_str.split(',')]
print(fish_list)
l = []
genrations = 1
while genrations <= 10:
    baby_fish_count = 0
    for i, fish in enumerate(fish_list):
        print(fish)
        print(f'fish type = {type(fish)}')
        if fish == 0:
            print(f'fish: {fish} == 0')
            baby_fish_count += 1
            fish[i] = 6
        else:
            print(f'fish: {fish} is not 0')
            fish = fish - 1
        print(f'after iteration {i}, `fish_list` = {fish_list}')
    new_fish = [8] * baby_fish_count
    if len(new_fish) > 0:
        fish_list.append(new_fish)
    print(f'fish_list after iteration {i}: {fish_list}')
    genrations += 1

print(fish_list)