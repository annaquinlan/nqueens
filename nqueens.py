# Written by Sophia Davis and Anna Quinlan, 4/27/14
import random
import sets

# Returns solution to for n by n board.
def nqueens(n):
    if n <= 3:
        return false
    # make the board
    board = []
    j = 0
    for i in range(0, n):
        board.append(range(j, j + n))
        j += n
    printboard(board, n)
    print
    assignment = []
    possible = [range(0, n*n)]
    print "placing queens"
    print backtrack(assignment, possible, n, board)

# with '0' as [0,0]
def getindex(i, n):
    return (i%n, i/n)

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

def printboard(board, n):
    for i in range(0, n):
        print board[i]
        
def backtrack(assignment, possible, n, board):
    print "---Starting iteration of backtrack"
    print assignment
    if len(assignment) == n:
        return assignment
    print "Options are"
    currentoptions = possible[-1]
    print possible
    print currentoptions
    print "---"
    # get variable to assign
    for loc in currentoptions:
        print "considering location " + str(loc)
        # if value is consistent with assignment
            # add {var = value} to assignment
        assignment.append(loc)
            # perform inference
        restricted = inference(board, loc, n, currentoptions)
        # if inference  not a failure
        if len(restricted) >= (n - len(assignment)):
            possible.append(restricted)
            result = backtrack(assignment, possible, n, board)
            print "this is result"
            print result
            if result:
                print "in if"
                return assignment
        # remove {var = value} and inferences from assignment
        print "BACKTRACK!!"
        assignment.pop()
        possible.pop()
    return False
## problem = it's not "popping" up far enough
    
# return all locations that can still have a queen    
def inference(board, i, n, possible):
    print "starting inference"
    possibleset = sets.Set(possible)
    rows = sets.Set(getrow(board, i, n))
    cols = sets.Set(getcol(board, i, n))
    ldiags = sets.Set(getdiagsleft(board, i, n))
    rdiags = sets.Set(getdiagsright(board, i, n))
    updated = possibleset.difference(rows).difference(cols).difference(ldiags).difference(rdiags)
    return list(updated)

nqueens(4)
