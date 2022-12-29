import sys
import os
import argparse
import requests
import time
import io
from pathlib import Path

ENV_FILEPATH = '.env'
DEFAULT_TEMPLATE_CODE = '''
import os

_heredir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(_heredir, 'input.txt')

with open(filename, 'r') as f:
    input_str = f.read()
'''

def get_dir_path(file: str):
    return os.path.dirname(os.path.realpath(file))

def get_list_data(module_path: str) -> list:
    """Read lines of the input file that corresponds to the module name."""
    with open(get_data_path(module_path), "r") as f:
        return [s.strip() for s in f.readlines()]

def get_input_string(module_path: str) -> str:
    with open(get_data_path(module_path), "r") as f:
        return f.read()

def get_data_path(module_path: str) -> str:
    """Input file path from `data/` that corresponds to the module name."""
    p = Path(module_path)
    return p.parent / "input.txt"

def _get_cookie_value() -> str:
    with open(ENV_FILEPATH) as f:
        return {'session' : f.read().strip()}

def get_input(year: int, day: int) -> str:
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    print(url)
    results = requests.get(url,
              cookies = _get_cookie_value(),
              headers = {'User-Agent' : 'ricko rick.d.ortega@gmail.com'})
    return results.content


def create_day_help():
    USAGE = """
    This command-line tool will create the scaffold of an Advent of Code puzzle
    solve. A .env file must exist in the main project directory containing the
    cookie found from a logged in web session for AoC. The .env file should look
    like this (only the cookie value):
    <cookie_value>\n\n
    To create a day use the following flags to create a directory structure and
    input data for a particular puzzle:
    --day: The day of the puzzle as a number (i.e. 5)
    --year: The 4-digit year of the puzzle (i.e. 2021)\n\n
    An to retrieve the puzzle for day 1 of 2021, your command would look like this:\n
    aoc-create-day --day 1 --year 2021
    """

    print(USAGE)

def create_day():
    if "-h" in sys.argv or "--help" in sys.argv:
        create_day_help()
        sys.exit()

    parser = argparse.ArgumentParser()
    parser.add_argument('--day', type=str, required=True)
    parser.add_argument('--year', type=str, required=True)
    args = parser.parse_args()

    day = str(args.day)
    year = str(args.year)

    day_file_str = f'day_{day.zfill(2)}'

    if not os.path.exists(day_file_str):
        os.mkdir(day_file_str)

    template_text = f'''#Advent of Code {year} day {day}{DEFAULT_TEMPLATE_CODE}
    '''

    with open(f'{day_file_str}/p1.py', 'w') as f:
        f.write(template_text)
    with open(f'{day_file_str}/p2.py', 'w') as f:
        f.write(template_text)

    day_int = int(args.day)
    year_int = int(args.year)

    for i in range(5):
        try:
            s = get_input(year_int, day_int)
        except requests.exceptions.RequestException as e:
            print(f'zzz: not ready yet: {e}')
            time.sleep(1)
        else:
            break
    else:
        raise SystemExit('timed out after attempting many times')

    with open(f'{day_file_str}/input.txt', 'wb') as f:
        f.write(s)

    lines = s.splitlines()
    if len(lines) > 10:
        for line in lines[:10]:
            print(line)
        print('...')
    else:
        print(lines[0][:80])
        print('...')

    return 0