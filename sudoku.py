# Sudoku Solver using Backtracking Algorithm

# Function to check if placing the number in the grid is valid
def is_valid(grid, row, col, num):
    # Check if num is not in the current row
    for i in range(9):
        if grid[row][i] == num:
            return False
    
    # Check if num is not in the current column
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # Check if num is not in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    
    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(grid):
    # Find an empty cell in the grid (represented by 0)
    empty_cell = find_empty(grid)
    if not empty_cell:
        # No empty cells means the puzzle is solved
        return True
    else:
        row, col = empty_cell
    
    # Try placing digits 1-9 in the empty cell
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            # Place the number if it's valid
            grid[row][col] = num
            
            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(grid):
                return True
            
            # Backtrack by resetting the cell
            grid[row][col] = 0
    
    return False

# Helper function to find an empty cell in the grid
def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)  # Return the position of the empty cell
    return None

# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Example unsolved Sudoku puzzle (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle and print the solution
if solve_sudoku(grid):
    print("Solved Sudoku grid:")
    print_grid(grid)
else:
    print("No solution exists")
