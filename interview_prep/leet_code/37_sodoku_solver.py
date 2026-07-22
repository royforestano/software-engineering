"""
37. Sudoku Solver

Difficulty: Hard
Link: https://leetcode.com/problems/sudoku-solver/description/


Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

# N is the number of empty cells
# Time: O(9^N) (worst), much faster in practice
# SPace: O(N) from the call stack

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = {i: set() for i in range(9)}
        cols = {j: set() for j in range(9)}
        boxes = {(i//3, j//3): set() for i in range(0,9,3) for j in range(0,9,3)}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i//3, j//3)].add(val)

        def backtrack(cells):
            if not cells:
                return True  # no empty cells left

            i, j = cells[0]
            box = (i//3, j//3)

            for num in '123456789':
                if num not in rows[i] and num not in cols[j] and num not in boxes[box]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)

                    if backtrack(cells[1:]):
                        return True

                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box].remove(num)

            return False

        empty = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '.']
        backtrack(empty)

