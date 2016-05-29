#import numpy as np
from scipy.sparse import dok_matrix
import row as r

def elimination(A):
    """
    Given a sparse dok_matrix returns the gauss eliminated sparse matrix
    """
    numRows, numCols = A.shape
    row,col = 0,0
    while col < numCols and row < numRows:
        nonzero_relative_col = A.getcol(col)[row:,:].nonzero()[0]
        if len(nonzero_relative_col)==0:
            col += 1
            continue
        first_nonzero = nonzero_relative_col[0]+row #conversion from relative to absolute
        if first_nonzero!=row:
            r.swap(A,row,first_nonzero)
        p = float(A[row,col]) #make p a float such that 1/p does not truncate to 0
        r.scale(A,row,1/p)

        for l in nonzero_relative_col: 
            if l!=0: # since l is realtive from offset row
                n = A[l+row,col]
                r.combine(A,l+row,row,-n)
        row += 1
        col += 1
    return A
