#!/usr/bin/env python

import sudolver

# sudoku = Sudoku([2, 9, 5, 7, 4, 3, 8, 6, 1, 4, 3, 1, 8, 6, 5, 9, 2, 7, 8, 7, 6, 1, 9, 2, 5, 4, 3, 3, 8, 7, 4, 5, 9, 2, 1, 6, 6, 1, 2, 3, 8, 7, 4, 9, 5, 5, 4, 9, 2, 1, 6, 7, 3, 8, 7, 6, 3, 5, 3, 4, 1, 8, 9, 9, 2, 8, 6, 7, 1, 3, 5, 4, 1, 5, 4, 9, 3, 8, 6, 7, 2])
renderer = sudolver.Renderer()
sudoku = sudolver.Sudoku([
    1, 3, None, 6, None, 9, None, None, 7,
    6, None, 8, None, 3, 4, 9, None, None,
    None, 7, None, 8, 1, None, None, None, None,
    None, None, None, None, None, None, 7, 8, 4,
    None, 4, None, None, None, None, None, 3, None,
    9, 2, 3, None, None, None, None, None, None,
    None, None, None, None, 5, 6, None, 9, None,
    None, None, 5, 9, 4, None, 6, None, 1,
    4, None, None, 1, None, 8, None, 2, 3])
solver = sudolver.Solver()

print("Initial puzzle")
print(renderer.render(sudoku))

solved = solver.solve(sudoku)

print("Solved puzzle")
print(renderer.render(solved))
