# Written by Sophia Davis and Anna Quinlan, 4/27/14

# Returns solution to for n by n board.
def nqueens(n):
    # make the board
    board = []
    j = 0
    for i in range(0, n):
        board.append(range(j, j + n))
        j += n
    printboard(board, n)
    print
    print "index of 14 is"
    getindex(14, n)
    print
    print "getting row of 14"
    getrow(board, 14, n)
    print
    print "getting col of 14"
    getcol(board, 14, n)
    print
    print "getting diagsleft of 14"
    getdiagsleft(board, 14, n)
    print "getting diagsright of 12"
    getdiagsright(board, 12, n)

# with '0' as [0,0]
def getindex(i, n):
    return (i%n, i/n)

def getrow(board, i, n):
    print board[i / n]

def getcol(board, i, n):
    col = []
    for j in range(0, n):
        col.append(board[j][i % n])
    print col

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
    print diags
        
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
    print diags

def printboard(board, n):
    for i in range(0, n):
        print board[i]
    
nqueens(5)
