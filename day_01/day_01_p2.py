from aoc_tools import get_list_data

input = get_list_data(__file__)
numbers = [int(line) for line in input]

def count_sliding_increases(s: list[int], slide_length: int) -> int:
    return sum(
        s[i] > s[i - slide_length] for i in range(slide_length, len(s))
        )

print(count_sliding_increases(numbers, 3))


