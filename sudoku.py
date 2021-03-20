import numpy as np
sudoku=[[0,1,0,2,0,0,3,0,0],
        [2,6,0,0,0,0,0,0,9],
        [9,0,0,0,1,0,2,0,4],
        [0,0,0,0,8,0,0,0,1],
        [0,0,6,0,0,0,5,0,0],
        [3,0,0,0,9,0,0,0,0],
        [6,0,2,0,7,0,0,0,8],
        [7,0,0,0,0,0,0,4,3],
        [0,0,8,0,0,5,0,1,0]]

def display():
    global sudoku
    print(np.matrix(sudoku))
        
def possible(y, x, n):
    global sudoku
    for i in range(9):
        if sudoku[y][i] == n:
            return False
    for j in range(9):
        if sudoku[j][x] == n:
            return False
    boxrow = (y//3)*3
    boxcol = (x//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[boxrow+i][boxcol+j] == n:
                return False
    return True

def solve():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] ==0:
                k = []
                for n in range(1,10):
                    if possible(y,x,n):
                        k.append(n)
                if len(k)==1:
                    sudoku[y][x] =k[0]
                else:
                    sudoku[y][x] =0
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                solve()
        

display()
solve()
display()




                        
    

