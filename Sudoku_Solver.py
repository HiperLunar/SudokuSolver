

def solve(sudoku):
    fix = [[False if col == 0 else True for col in row] for row in sudoku]
    # True if the square should not be tested

    def get_row(sudoku, row, col):
        return [sudoku[row][x] if x != col else 0 for x in range(9)]
    # Get row of position and replace position to 0

    def get_col(sudoku, row, col):
        return [sudoku[y][col] if y != row else 0 for y in range(9)]
    # Get column of position and replace position to 0

    def get_square(sudoku, row, col):
        x, y = (col//3)*3, (row//3)*3
        return [sudoku[y+(i//3)][x+(i%3)] if y+(i//3) != row or x+(i%3) != col else 0 for i in range(9)]
    # Get 3x3 square of position and replace position to 0

    def check_pos(sudoku, row, col):
        n = sudoku[row][col]
        if n == 0:
            return True
        else:
            return n not in get_row(sudoku, row, col) and n not in get_col(sudoku, row, col) and n not in get_square(sudoku, row, col)
    # Check specific position validity

    def check_game(sudoku):
        for row in range(9):
            for col in range(9):
                if not check_pos(sudoku, row, col):
                    return False
        return True
    # Check all game

    # This is where the magic begins...
    # This is a recursive function that check all possibilities
    def test(sudoku, row, col):
        if row > 8:
            return sudoku   # If row > 8 means the game is solved and the result is backward propagated
        if fix[row][col]:
            return test(sudoku, row + (col+1)//9, (col+1) % 9)  # If the position is fixed, step one
        for i in range(1, 10):  # Try all 9 possibilities
            attempt = [[sudoku[y][x] if y != row or x != col else i for x in range(9)] for y in range(9)]
            # Copy the game and replace the guess
            if check_game(attempt):     # Check if the guess is valid
                result = test(attempt, row + (col+1)//9, (col+1) % 9)   # If true, step one
                if result:
                    return result  # If not none, back propagate
        return None     # If any number is possible, step back and try again

    return test(sudoku, 0, 0)


if __name__ == "__main__":
    sudoku = (
        (5, 3, 0, 0, 7, 0, 0, 0, 0),
        (6, 0, 0, 1, 9, 5, 0, 0, 0),
        (0, 9, 8, 0, 0, 0, 0, 6, 0),
        (8, 0, 0, 0, 6, 0, 0, 0, 3),
        (4, 0, 0, 8, 0, 3, 0, 0, 1),
        (7, 0, 0, 0, 2, 0, 0, 0, 6),
        (0, 6, 0, 0, 0, 0, 2, 8, 0),
        (0, 0, 0, 4, 1, 9, 0, 0, 5),
        (0, 0, 0, 0, 8, 0, 0, 7, 9)
    )   # Example of sudoku

    solved = solve(sudoku)
    for row in solved:
        for col in row:
            print(col, end=' | ')
        print()
