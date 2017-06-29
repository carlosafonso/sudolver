#!/usr/bin/env python
from copy import deepcopy


class Solver(object):

    def solve(self, sudoku):
        solvee = deepcopy(sudoku)
        while not solvee.is_solved():
            for row in range(9):
                for col in range(9):
                    if solvee.get_cell((row, col)) is None:
                        options = self.get_options_for_cell(solvee, row, col)
                        if len(options) == 0:
                            raise Exception("No valid options for this cell")
                        if len(options) == 1:
                            value = options.pop()
                            solvee.set_cell((row, col), value)
        return solvee

    def get_options_for_cell(self, sudoku, row, col):
        in_row = sudoku.get_row(row)
        in_col = sudoku.get_column(col)
        in_quadrant = sudoku.get_quadrant_for_cell((row, col))
        taken = set(in_row + in_col + in_quadrant)
        return set(range(1, 10)).difference(taken)


class Sudoku(object):

    def __init__(self, initial_state=None):
        self.__initialize_state(initial_state)

    def __initialize_state(self, initial_state=None):
        if initial_state:
            self.state = initial_state
        else:
            self.state = [None for i in range(81)]

    def get_all_cells(self):
        return self.state

    def get_cell(self, cell):
        row, col = cell
        if not 0 <= row <= 8 or not 0 <= col <= 8:
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

    def get_quadrant_for_cell(self, cell):
        row, col = cell
        return self.get_quadrant(3 * (row // 3) + (col // 3))

    def set_cell(self, cell, value):
        row, col = cell
        if not 0 <= row <= 8 or not 0 <= col <= 8:
            raise ValueError("Cell ({}, {}) out of valid range [(0,0) - (8,8)]".format(row, col))
        self.state[9 * row + col] = value

    def is_solved(self):
        for cell in self.state:
            if cell is None:
                return False
        return True


class Renderer(object):

    def render(self, sudoku):
        template = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}"
        return template.format(self.__get_top_border(),
                               self.__get_row(0, sudoku),
                               self.__get_middle_border_light(),
                               self.__get_row(1, sudoku),
                               self.__get_middle_border_light(),
                               self.__get_row(2, sudoku),
                               self.__get_middle_border_bold(),
                               self.__get_row(3, sudoku),
                               self.__get_middle_border_light(),
                               self.__get_row(4, sudoku),
                               self.__get_middle_border_light(),
                               self.__get_row(5, sudoku),
                               self.__get_middle_border_bold(),
                               self.__get_row(6, sudoku),
                               self.__get_middle_border_light(),
                               self.__get_row(7, sudoku),
                               self.__get_middle_border_light(),
                               self.__get_row(8, sudoku),
                               self.__get_bottom_border())

    def __get_top_border(self):
        return "╔═══════════╦═══════════╦═══════════╗"

    def __get_bottom_border(self):
        return "╚═══════════╩═══════════╩═══════════╝"

    def __get_middle_border_light(self):
        return "║───┼───┼───║───┼───┼───║───┼───┼───║"

    def __get_middle_border_bold(self):
        return "╠═══════════╬═══════════╬═══════════╣"

    def __get_row(self, row, sudoku):
        row = [" " if not i else str(i) for i in sudoku.get_row(row)]
        return "║ {} ║ {} ║ {} ║".format(" │ ".join(row[0:3]),
                                         " │ ".join(row[3:6]),
                                         " │ ".join(row[6:9]))
