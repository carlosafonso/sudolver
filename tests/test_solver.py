from context import sudolver
import unittest


class TestSolver(unittest.TestCase):

    def setUp(self):
        self.solver = sudolver.Solver()

    def test_solve(self):
        """solve should return a solved sudoku if a solution exists"""
        sudoku = sudolver.Sudoku([1, 3, None, 6, None, 9, None, None, 7, 6, None, 8, None, 3, 4, 9, None, None, None, 7, None, 8, 1, None, None, None, None, None, None, None, None, None, None, 7, 8, 4, None, 4, None, None, None, None, None, 3, None, 9, 2, 3, None, None, None, None, None, None, None, None, None, None, 5, 6, None, 9, None, None, None, 5, 9, 4, None, 6, None, 1, 4, None, None, 1, None, 8, None, 2, 3])
        expected = [1, 3, 4, 6, 2, 9, 8, 5, 7, 6, 5, 8, 7, 3, 4, 9, 1, 2, 2, 7, 9, 8, 1, 5, 3, 4, 6, 5, 6, 1, 2, 9, 3, 7, 8, 4, 8, 4, 7, 5, 6, 1, 2, 3, 9, 9, 2, 3, 4, 8, 7, 1, 6, 5, 7, 1, 2, 3, 5, 6, 4, 9, 8, 3, 8, 5, 9, 4, 2, 6, 7, 1, 4, 9, 6, 1, 7, 8, 5, 2, 3]

        solved = self.solver.solve(sudoku)

        self.assertEqual(expected, solved.get_all_cells())

if __name__ == '__main__':
    unittest.main()
