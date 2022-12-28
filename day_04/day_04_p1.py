#Advent of Code 2021 day 4
from __future__ import annotations
import os

_heredir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(_heredir, 'input.txt')

with open(filename, 'r') as f:
    input_str = f.read()

# input_str = '''\
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# '''

numbers, *input = input_str.split('\n\n')

class Board():

    def __init__(self, left, ints, winner=False):
        self.left: set[int] = left
        self.ints: list[int] = ints
        self.winner: bool = winner
    def __str__(self):
        return (
            f'Board object\nNumbers left: {self.left}\n'
            f'Initial Board numbers: {self.ints}')

    @property
    def has_won(self):
        return self.winner

    def discard_number(self, number: int):
        self.left.discard(number)
        self.check_rows()
        self.check_cols()
        if self.winner:
            print(f'\t\t - WINNER - \n\t\tWinning number = {number}')
            print(f'sum of left = {sum(self.left)}')
            print(f'sum(self.left) * number = {sum(self.left) * number}')
    
    def check_rows(self) -> bool:
        for i in range(5):
            num_found = 0
            for j in range(5):
                number = self.ints[i * 5 + j]
                if number in self.left:
                    num_found += 1
            if num_found == 0:
                self.winner = True
         
    def check_cols(self) -> bool:
        for i in range(5):
            num_found = 0
            for j in range(5):
                number_to_check = self.ints[i + 5 * j]
                if number_to_check in self.left:
                    num_found += 1
            if num_found == 0:
                self.winner = True

    @classmethod
    def parse(cls, board: str) -> Board:
        cls.ints = [int(s) for s in board.split()]
        cls.left = set(cls.ints)
        return cls(cls.left, cls.ints)

boards = [Board.parse(board) for board in input]
ints = [int(s) for s in numbers.split(',')]

def get_first_winning_board(ints: list(str), boards: list(Board)) -> Board:
    for number in ints:
        for board in boards:
            board.discard_number(number)
            if board.winner:
                return (board, number)
    raise AssertionError('There really should be a winner')

def get_winning_number(board: Board, number: int) -> int:
    return sum(board.left) * number

winner_board, winning_number = get_first_winning_board(ints, boards)
print(str(winner_board))
winning_number = get_winning_number(winner_board, winning_number)
print(f'winning number is {winning_number}')


# def get_winner_list(ints: list(str), boards: list(Board)) -> list(Board):
#     winner_list = []    
#     for board in boards:
#         for num in ints:
#             board.discard_number(num)
#             if board.winner:
#                 winner_list.append(board)
#                 break
#     return winner_list

# def get_last_winner(boards: list(Board)) -> Board:
#     return boards[-1]

# def calculate_score(board: Board):
#     for number in ints:
#         board.discard_number(number)
#         if board.winner:
#             return sum(board.left) * number

# winner_list = get_winner_list(ints, boards)
# last_winner = get_last_winner(winner_list)
# print(calculate_score(last_winner))