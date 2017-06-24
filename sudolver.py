#!/usr/bin/env python
from copy import deepcopy


class Solver(object):

    def solve(self, sudoku):
        solvee = deepcopy(sudoku)
        while not self.is_solved(solvee):
            for row in range(9):
                for col in range(9):
                    # print("Checking ({},{})".format(row, col))
                    if solvee.get_cell((row, col)) is None:
                        options = self.get_options_for_cell(solvee, row, col)
                        if len(options) == 0:
                            raise Exception("No valid options for this cell")
                        if len(options) == 1:
                            value = options.pop()
                            # print("Cell has only one option: {}".format(value))
                            solvee.set_cell(row, col, value)
                            self.__print_puzzle(solvee)
                        else:
                            pass
                            # print("Cell has more than one option: {}".format(options))
                    else:
                        pass
                        # print("Cell already filled")
            print("Evaluation round complete")
        print("Sudoku is solved")
        return sudoku

    def is_solved(self, sudoku):
        for cell in sudoku.state:
            if cell is None:
                return False
        return True

    def get_options_for_cell(self, sudoku, row, col):
        in_row = sudoku.get_row(row)
        in_col = sudoku.get_column(col)
        in_quadrant = sudoku.get_quadrant(self.__quadrant_for_row_col(row, col))
        taken = set(in_row + in_col + in_quadrant)
        # print(in_row, in_col, in_quadrant, taken)
        options = set(range(1, 10)).difference(taken)
        return options

    def __quadrant_for_row_col(self, row, col):
        if row <= 2:
            if col >= 6:
                return 2
            if col >= 3:
                return 1
            return 0
        if row <= 5:
            if col >= 6:
                return 5
            if col >= 3:
                return 4
            return 3
        if col >= 6:
            return 8
        if col >= 3:
            return 7
        return 6

    def __print_puzzle(self, sudoku):
        string = "\n\n"
        for (idx, val) in enumerate(sudoku.state):
            if idx % 9 == 0:
                string = string + "\n"
            string = string + " {} ".format(val if val else " ")
        print(string)


class Sudoku(object):

    def __init__(self, initial_state=None):
        self.__initialize_state(initial_state)

    def __initialize_state(self, initial_state=None):
        if initial_state:
            self.state = initial_state
        else:
            self.state = [None for i in range(81)]

    def get_cell(self, cell):
        row, col = cell
        if row < 0 or col < 0 or row > 8 or col > 8:
            raise ValueError("Cell ({}, {}) out of valid range [(0,0) - (8,8)]".format(row, col))
        return self.get_row(row)[col]

    def get_row(self, row):
        if 0 <= row <= 8:
            return self.state[row * 9:row * 9 + 9]
        raise ValueError("Row {} out of valid range [0-8]".format(row))

    def get_column(self, col):
        if 0 <= col <= 8:
            return [self.state[i] for i in range(col, col + 9 * 9, 9)]
        raise ValueError("Column {} out of valid range [0-8]".format(col))

    def get_quadrant(self, quadrant):
        if 0 <= quadrant <= 8:
            idx = (quadrant % 3) * 3 + (quadrant // 3) * 27
            return self.state[idx:idx + 3] + self.state[idx + 9:idx + 12] + self.state[idx + 18:idx + 21]
        raise ValueError("Quadrant {} out of valid range [0-8]".format(quadrant))

    def set_cell(self, row, col, value):
        self.state[9 * row + col] = value
