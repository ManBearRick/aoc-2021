#Advent of Code 2021 day 05
import os
from collections import Counter
from typing import Tuple

_heredir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(_heredir, 'input.txt')

with open(filename, 'r') as f:
    input_str = f.read()

# input_str = '''\
# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# '''

points: Counter[Tuple[int, int]] = Counter()
    
for line in input_str.splitlines():
    start, end = line.split(' -> ')
    x1_s, y1_s = start.split(',')
    x2_s, y2_s = end.split(',')
    x1, y1, x2, y2 = int(x1_s), int(y1_s), int(x2_s), int(y2_s)
    
    if x1 == x2:
        print(f'this line is horizontal: \n{x1, y1, x2, y2}')
        for y in range(min(y1, y2), max(y1, y2) + 1):
            print(f'y points {y}')
            points[x1, y] += 1

    elif y1 == y2:
        print(f'this line is vertical: \n{x1, y1, x2, y2}')
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points[x, y1] += 1
    else:
        print(f'this line is diagonal: \n{x1, y1, x2, y2}')

count = 0
for point, value in points.most_common():
    if value > 1:
        count += 1
print(count)


    
    