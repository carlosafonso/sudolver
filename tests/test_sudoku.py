from context import sudolver
import unittest


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.sudoku = sudolver.Sudoku([2, 9, 5, 7, 4, 3, 8, 6, 1, 4, 3, 1, 8, 6, 5, 9, 2, 7, 8, 7, 6, 1, 9, 2, 5, 4, 3, 3, 8, 7, 4, 5, 9, 2, 1, 6, 6, 1, 2, 3, 8, 7, 4, 9, 5, 5, 4, 9, 2, 1, 6, 7, 3, 8, 7, 6, 3, 5, 3, 4, 1, 8, 9, 9, 2, 8, 6, 7, 1, 3, 5, 4, 1, 5, 4, 9, 3, 8, 6, 7, 2])

    def test_get_all_cells(self):
        expected = [2, 9, 5, 7, 4, 3, 8, 6, 1, 4, 3, 1, 8, 6, 5, 9, 2, 7, 8, 7, 6, 1, 9, 2, 5, 4, 3, 3, 8, 7, 4, 5, 9, 2, 1, 6, 6, 1, 2, 3, 8, 7, 4, 9, 5, 5, 4, 9, 2, 1, 6, 7, 3, 8, 7, 6, 3, 5, 3, 4, 1, 8, 9, 9, 2, 8, 6, 7, 1, 3, 5, 4, 1, 5, 4, 9, 3, 8, 6, 7, 2]
        self.assertEqual(expected, self.sudoku.get_all_cells())

    def test_get_cell(self):
        """get_cell should return the value in the given cell"""
        self.assertEqual(5, self.sudoku.get_cell((6, 3)))
        self.assertEqual(1, self.sudoku.get_cell((3, 7)))
        self.assertEqual(2, self.sudoku.get_cell((8, 8)))

    def test_get_cell_with_negative_row(self):
        """get_cell should fail if the given row is negative"""
        self.assertRaises(ValueError, self.sudoku.get_cell, (-1, 0))

    def test_get_cell_with_too_large_row(self):
        """get_cell should fail if the given row is greater than 8"""
        self.assertRaises(ValueError, self.sudoku.get_cell, (9, 0))

    def test_get_cell_with_negative_column(self):
        """get_cell should fail if the given column is negative"""
        self.assertRaises(ValueError, self.sudoku.get_cell, (0, -1))

    def test_get_cell_with_too_large_column(self):
        """get_cell should fail if the given column is greater than 8"""
        self.assertRaises(ValueError, self.sudoku.get_cell, (0, 9))

    def test_set_cell(self):
        """set_cell should set the given value in the cell"""
        self.sudoku.set_cell((2, 2), 0)
        self.assertEqual(0, self.sudoku.get_cell((2, 2)))

    def test_set_cell_with_negative_row(self):
        """set_cell should fail if the given row is negative"""
        self.assertRaises(ValueError, self.sudoku.set_cell, (-1, 0), 0)

    def test_set_cell_with_too_large_row(self):
        """set_cell should fail if the given row is greater than 8"""
        self.assertRaises(ValueError, self.sudoku.set_cell, (9, 0), 0)

    def test_set_cell_with_negative_column(self):
        """set_cell should fail if the given column is negative"""
        self.assertRaises(ValueError, self.sudoku.set_cell, (0, -1), 0)

    def test_set_cell_with_too_large_column(self):
        """set_cell should fail if the given column is greater than 8"""
        self.assertRaises(ValueError, self.sudoku.set_cell, (0, 9), 0)

    def test_get_row(self):
        """get_row should return all values in the row"""
        expected = [8, 7, 6, 1, 9, 2, 5, 4, 3]
        self.assertEqual(expected, self.sudoku.get_row(2))

    def test_get_row_with_negative_index(self):
        """get_row should fail if the given row is negative"""
        self.assertRaises(ValueError, self.sudoku.get_row, -1)

    def test_get_row_with_too_large_index(self):
        """get_row should fail if the given row is greater than 8"""
        self.assertRaises(ValueError, self.sudoku.get_row, 9)

    def test_get_column(self):
        """get_column should return all values in the column"""
        expected = [8, 9, 5, 2, 4, 7, 1, 3, 6]
        self.assertEqual(expected, self.sudoku.get_column(6))

    def test_get_column_with_negative_index(self):
        """get_column should fail if the given column is negative"""
        self.assertRaises(ValueError, self.sudoku.get_column, -1)

    def test_get_column_with_too_large_index(self):
        """get_column should fail if the given column is greater than 8"""
        self.assertRaises(ValueError, self.sudoku.get_column, 9)

    def test_get_quadrant(self):
        """get_quadrant should return all values in the quadrant"""
        expected = [4, 5, 9, 3, 8, 7, 2, 1, 6]
        self.assertEqual(expected, self.sudoku.get_quadrant(4))

    def test_get_quadrant_for_cell(self):
        """get_quadrant_for_cell should return all values in the quadrant where
        the given cell is located
        """
        expected = [4, 5, 9, 3, 8, 7, 2, 1, 6]
        self.assertEqual(expected, self.sudoku.get_quadrant_for_cell((5, 3)))

    def test_get_quadrant_with_negative_index(self):
        """get_quadrant should fail if the given quadrant is negative"""
        self.assertRaises(ValueError, self.sudoku.get_quadrant, -1)

    def test_get_quadrant_with_too_large_index(self):
        """get_quadrant should fail if the given quadrant is greater than 8"""
        self.assertRaises(ValueError, self.sudoku.get_quadrant, 9)

    def test_is_solved_when_puzzle_is_solved(self):
        """is_solved should return true if sudoku is solved"""
        self.assertTrue(self.sudoku.is_solved())

    def test_is_solved_when_puzzle_is_not_solved(self):
        """is_solved should return false if sudoku is not solved"""
        sudoku = sudolver.Sudoku()
        self.assertFalse(sudoku.is_solved())

if __name__ == '__main__':
    unittest.main()
