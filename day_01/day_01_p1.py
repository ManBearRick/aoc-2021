from aoc_tools import get_list_data

def count_increases() -> int:
    input = get_list_data(__file__)
    numbers = [int(line) for line in input]
    return sum(1 for i in range(1, len(numbers)) if numbers[i] > numbers[i-1])

print(count_increases())