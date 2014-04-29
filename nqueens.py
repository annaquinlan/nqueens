# N-Queens Problem
# Written by Sophia Davis and Anna Quinlan, 4/27/14

import sets

# Returns n-queens solution for n by n board.
def nqueens(n):
    if n <= 3:
        return false
    # Make the board as a list of rows.
    board = []
    j = 0
    for i in range(0, n):
        board.append(range(j, j + n))
        j += n
    
    # Assignment list contains queen locations. Options contains lists of possible assignments
    # given already assigned queen locations.
    # i.e. Options[1] is remaining "safe" locations after placing one queen.
    assignment = []
    options = [range(0, n*n)]
    return backtrack(assignment, options, n, board)

# Returns the (x,y) coordinates of a number on the board with '0' as [0,0]
def getindex(i, n):
    return (i%n, i/n)

# Given a number on the board, these functions return numbers in the same row, column, or diagonals.
def getrow(board, i, n):
    return board[i / n]

def getcol(board, i, n):
    col = []
    for j in range(0, n):
        col.append(board[j][i % n])
    return col

def getdiagsleft(board, i, n):
    index = getindex(i, n)
    x = index[0]
    y = index[1]
    diags = [i]
    while (x > 0 and y > 0):
        new = board[y - 1][x - 1]
        diags.append(new)
        x -= 1
        y -= 1
    x = index[0]
    y = index[1]
    while (x < (n - 1) and y < (n - 1)):
        new = board[y + 1][x + 1]
        diags.append(new)
        x += 1
        y += 1
    return diags
        
def getdiagsright(board, i, n):
    index = getindex(i, n)
    x = index[0]
    y = index[1]
    diags = [i]
    while (x < (n - 1) and y > 0):
        new = board[y - 1][x + 1]
        diags.append(new)
        x += 1
        y -= 1
    x = index[0]
    y = index[1]
    while (x > 0 and y < (n - 1)):
        new = board[y + 1][x - 1]
        diags.append(new)
        x -= 1
        y += 1
    return diags

# Prints the board
def printboard(board, n):
    for i in range(0, n):
        print board[i]

# Implementation of backtracking search        
def backtrack(assignment, options, n, board):
    if len(assignment) == n:
        return assignment
    
    # Given last queen assignment, the last list in 'options' contains the remaining "safe" locations
    # to potentially put next queen. 
    currentoptions = options[-1]
    
    # Get a "safe" location
    for loc in currentoptions:
        
        # Add location to assignment
        assignment.append(loc)
        
        # Perform inference
        safe = inference(board, loc, n, currentoptions)
        
        # If inference not a failure (there are still more "safe" locations than queens we need to place)
        if len(safe) >= (n - len(assignment)):
            options.append(safe)
            result = backtrack(assignment, options, n, board)
            if result:
                return assignment
        
        # Get rid of last queen assignment if can't go further
        assignment.pop()
    return False
    
# Return all "safe" locations that can still have a queen  
# We used sets to filter locations that can no longer have a queen
def inference(board, i, n, options):
    optionsset = sets.Set(options)
    rows = sets.Set(getrow(board, i, n))
    cols = sets.Set(getcol(board, i, n))
    ldiags = sets.Set(getdiagsleft(board, i, n))
    rdiags = sets.Set(getdiagsright(board, i, n))
    updated = optionsset.difference(rows).difference(cols).difference(ldiags).difference(rdiags)
    return list(updated)

# Test:
# print nqueens(8)
