"""
This module solves day 4 of the advent of code challenge.
"""
from icecream import ic


def day_4_get_input(filename):
    """
    This functions gets the input
    """
    with open(filename) as file_input:
        data = file_input.readlines()

    drawn_numbers = [int(number) for number in data[0].split(",")]
    boards = []
    matrix = []
    for i in range(2, len(data)):
        if data[i] == "\n":
            boards.append(matrix)
            matrix = []
        else:
            matrix.append(
                [int(number) for number in list(filter(None, data[i].split(" ")))]
            )

    return drawn_numbers, boards


def mark_number(num, board):
    """
    This functions returns the board with the number given marked as seen
    """
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if board[i][j] == num:
                board[i][j] = "V"
    return board


def sum_unmarked_values(board):
    """
    This functions returns the sum of unmarked values in a board.
    """
    my_sum = 0
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if board[i][j] != "V":
                my_sum += board[i][j]
    return my_sum


def check_for_victory(board):
    """
    This functions checks if a board is in a victory condition.
    """
    for i in range(5):
        if (
            board[i][0] == "V"
            and board[i][1] == "V"
            and board[i][2] == "V"
            and board[i][3] == "V"
            and board[i][4] == "V"
        ):
            return True
        if (
            board[0][i] == "V"
            and board[1][i] == "V"
            and board[2][i] == "V"
            and board[3][i] == "V"
            and board[4][i] == "V"
        ):
            return True
    return False


def day_4_p1(drawn_numbers, boards):
    """
    This functions solves part 1 of the challenge
    """
    for value in drawn_numbers:
        for i, _ in enumerate(boards):
            boards[i] = mark_number(value, boards[i])
            if check_for_victory(boards[i]):
                return value, sum_unmarked_values(boards[i])
    return None


def day_4_p2(drawn_numbers, boards):
    """
    This functions solves part 2 of the challenge
    """
    has_won = [False for _ in range(len(boards))]
    for val in drawn_numbers:
        for i, _ in enumerate(boards):
            boards[i] = mark_number(val, boards[i])
            if check_for_victory(boards[i]):
                has_won[i] = True
                if sum(has_won) == len(boards):
                    return val, sum_unmarked_values(boards[i])
    return None


a, b = day_4_get_input("day_4_input.txt")
number, unmarked_sum = day_4_p2(a, b)
ic(number, unmarked_sum, number * unmarked_sum)
