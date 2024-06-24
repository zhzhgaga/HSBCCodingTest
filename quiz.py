def reverse_list(l: list):
    """

    TODO: Reverse a list without using any built in functions

    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """

    l_len = len(l)
    return [l[i] for i in range(l_len - 1, -1, -1)]
    # return l[::-1]


def solve_sudoku(matrix):
    """

    TODO: Write a programme to solve 9x9 Sudoku board.

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers
    so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is
    also an excellent brain game.

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """

    row_list, column_list, block_list = init_row_column_block(matrix, 9)
    bank_list = init_blank_list(matrix, row_list, column_list, block_list, 9)
    if check_matrix(row_list, column_list, block_list, bank_list) is False:
        return False
    blank = bank_list[0]
    if len(blank.input_list) == 1:
        matrix[blank.row_index][blank.column_index] = blank.input_list[0]
        return solve_sudoku(matrix)
    else:
        temp_matrix = list(matrix)
        for i in blank.input_list:
            matrix[blank.row_index][blank.column_index] = i
            if solve_sudoku == 0:
                matrix = temp_matrix
        return True


class Blank:

    def __init__(self, row_index, column_index, block_index, input_list):
        self.row_index = row_index
        self.column_index = column_index
        self.block_index = block_index
        self.input_list = input_list


def init_row_column_block(matrix, dimension=9):
    row_list, column_list, block_list = [], [], []
    for i in range(dimension):
        row_list.append([])
        column_list.append([])
        block_list.append([])

    for row_index in range(dimension):
        for column_index in range(dimension):
            v = matrix[row_index][column_index]
            if v == 0:
                continue
            row_list[row_index].append(v)
            column_list[column_index].append(v)
            block_index = cal_block_index(row_index, column_index)
            block_list[block_index].append(v)

    return row_list, column_list, block_list


def init_blank_list(matrix, row_list, column_list, block_list, dimension=9):
    blank_list = []
    for row_index in range(dimension):
        for column_index in range(dimension):
            v = matrix[row_index][column_index]
            if v != 0:
                continue
            block_index = cal_block_index(row_index, column_index)
            # [i for i in range(1, 10, 1)]
            input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for row_data in row_list[row_index]:
                if row_data in input_list:
                    input_list.remove(row_data)
            for column_data in column_list[column_index]:
                if column_data in input_list:
                    input_list.remove(column_data)
            for block_data in block_list[block_index]:
                if block_data in input_list:
                    input_list.remove(block_data)
            blank = Blank(row_index, column_index, block_index, input_list)
            blank_list.append(blank)
        blank_list.sort(key=lambda l: len(l.input_list))
    return blank_list


def cal_block_index(i, j):
    block_index, row_index, column_index = 0, i // 3, j // 3
    if row_index == 0 and column_index == 0:
        block_index = 0
    elif row_index == 0 and column_index == 1:
        block_index = 1
    elif row_index == 0 and column_index == 2:
        block_index = 2

    elif row_index == 1 and column_index == 0:
        block_index = 3
    elif row_index == 1 and column_index == 1:
        block_index = 4
    elif row_index == 1 and column_index == 2:
        block_index = 5

    elif row_index == 2 and column_index == 0:
        block_index = 6
    elif row_index == 2 and column_index == 1:
        block_index = 7
    # elif row_index == 2 and column_index == 2:
    else:
        block_index = 8
    return block_index


def check_matrix(row_list, column_list, block_list, bank_list):
    # check row
    for r in row_list:
        if len(row_list) != len(r):
            print('row_list is ' + row_list)
            return False
    # check column
    for c in column_list:
        if len(column_list) != len(c):
            print('column_list is ' + column_list)
            return False
    for b in block_list:
        if len(block_list) != len(b):
            print('block_list is ' + block_list)
            return False
    # check bank.input_list
    for b in bank_list:
        if len(b.input_list) == 0:
            print('input_list is ' + b.input_list)
            return False
    return True
