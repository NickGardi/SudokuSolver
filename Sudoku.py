# backtracking algorithm to solve sudoku puzzles

puzzle = [[5,1,7,6,0,0,0,3,4],
           [2,8,9,0,0,4,0,0,0],
           [3,4,6,2,0,5,0,9,0],
           [6,0,2,0,0,0,0,1,0],
           [0,3,8,0,0,6,0,4,7],
           [0,0,0,0,0,0,0,0,0],
           [0,9,0,0,0,0,0,7,8],
           [7,0,3,4,0,0,5,6,0],
           [0,0,0,0,0,0,0,0,0]]


# formatting the puzzle to look readable
def print_puzzle(puzzle):
    print("-"*37)
    # use enumerate to iterate over the rows and get the index of each row
    for i, row in enumerate(puzzle):
        # replacing 0s with " " and printing the rest of the numbers
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        # formatting
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")


def is_assigned(row,col):
    assigned = 0
    for i in range(9):
        for j in range(9):
            # if cell is empty (has a zero
            if puzzle[i][j] == 0:
                row = i
                col = j
                assigned = 1
                x = [-1, -1, assigned]
                return x

# check if a value can be put in a cell or not
def is_value_good(value, row, col):
    for i in range(9):
        if puzzle[row][i] == value:
            return False
    for i in range(9):
        if puzzle[i][col] == value:
            return False
    row_start = (row//3)*3
    col_start = (col//3)*3;
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if puzzle[i][j] == value:
                return False
    return True


def solve():
    row = 0
    col = 0
    #if all cells are assigned then the sudoku is already solved
    #pass by reference because number_unassigned will change the values of row and col
    a = is_assigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    #number between 1 to 9
    for i in range(1,10):
        #if we can assign i to the cell or not
        #the cell is matrix[row][col]
        if is_value_good(i, row, col):
            puzzle[row][col] = i
            #backtracking
            if solve():
                return True
            #f we can't proceed with this solution
            #reassign the cell
            puzzle[row][col]=0
    return False


print_puzzle(puzzle)

if(solve()):
    print(puzzle)
else:
    print("No solution found")
