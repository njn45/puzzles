"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Example 1:

Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below: 

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution.
"""

class Solution:

    def solve_sudoku(board:list[list[str]]) -> list[list[str]]:
        
        def possible_number(row:int, column:int, number:str) -> bool:
            
            # check column but fix the row
            if any(board[row][c] == number for c in range(9)):
                return False
            
            # check the rows but fix the column
            if any(board[r][column] == number for r in range(9)):
                return False
            
            #check the square that contains board[row][col]
            row_square, col_square = (row//3) * 3 , (column//3) * 3
            for r in range(3):
                for c in range(3):
                    if board[row_square + r][col_square + c] == number:
                        return False
            
            # number is not in the row, column or square so its valid
            return True
        
        def solve(row:int, col:int) -> bool:
            if (row == 8 and col == 9): return True # End of the board so stop back tracking. we've solved the sudoku
            
            if col == 9: # we've finished the current row and need to move onto the next one.
                row += 1
                col = 0
            
            if board[row][col] != ".": # we have a value for this location so we should move to the next column
                return solve(row,col + 1)
            
            for num in map(str,range(1,10)):
                
                if possible_number(row,col,num):
                    board[row][col] = num # number is valid so change the board to that

                    if solve(row,col + 1): # we've found a valid number so we have the same problem again but with 1 less number to find.
                        return True # we've completed the sudoku.
                

                board[row][col] = "." # number was not valid OR we failed to solve the sudoku with the possible number
            
            return False # No numbers were valid so we need to backtrack

        solve(0,0) # start at the begining of the board
        return board

def main():
    assert Solution.solve_sudoku([['3', '.', '6', '5', '.', '8', '4', '.', '.'], ['5', '2', '.', '.', '.', '.', '.', '.', '.'], ['.', '8', '7', '.', '.', '.', '.', '3', '1'], ['.', '.', '3', '.', '1', '.', '.', '8', '.'], ['9', '.', '.', '8', '6', '3', '.', '.', '5'], ['.', '5', '.', '.', '9', '.', '6', '.', '.'], ['1', '3', '.', '.', '.', '.', '2', '5', '.'], ['.', '.', '.', '.', '.', '.', '.', '7', '4'], ['.', '.', '5', '2', '.', '6', '3', '.', '.']]) == [['3', '1', '6', '5', '7', '8', '4', '9', '2'], ['5', '2', '9', '1', '3', '4', '7', '6', '8'], ['4', '8', '7', '6', '2', '9', '5', '3', '1'], ['2', '6', '3', '4', '1', '5', '9', '8', '7'], ['9', '7', '4', '8', '6', '3', '1', '2', '5'], ['8', '5', '1', '7', '9', '2', '6', '4', '3'], ['1', '3', '8', '9', '4', '7', '2', '5', '6'], ['6', '9', '2', '3', '5', '1', '8', '7', '4'], ['7', '4', '5', '2', '8', '6', '3', '1', '9']]
    assert Solution.solve_sudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) == [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    assert Solution.solve_sudoku([['2', '5', '.', '.', '3', '.', '9', '.', '1'], ['.', '1', '.', '.', '.', '4', '.', '.', '.'], ['4', '.', '7', '.', '.', '.', '2', '.', '8'], ['.', '.', '5', '2', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '9', '8', '1', '.', '.'], ['.', '4', '.', '.', '.', '3', '.', '.', '.'], ['.', '.', '.', '3', '6', '.', '.', '7', '2'], ['.', '7', '.', '.', '.', '.', '.', '.', '3'], ['9', '.', '3', '.', '.', '.', '6', '.', '4']]) == [['2', '5', '8', '7', '3', '6', '9', '4', '1'], ['6', '1', '9', '8', '2', '4', '3', '5', '7'], ['4', '3', '7', '9', '1', '5', '2', '6', '8'], ['3', '9', '5', '2', '7', '1', '4', '8', '6'], ['7', '6', '2', '4', '9', '8', '1', '3', '5'], ['8', '4', '1', '6', '5', '3', '7', '2', '9'], ['1', '8', '4', '3', '6', '9', '5', '7', '2'], ['5', '7', '6', '1', '4', '2', '8', '9', '3'], ['9', '2', '3', '5', '8', '7', '6', '1', '4']]

if __name__ == "__main__":
    main()