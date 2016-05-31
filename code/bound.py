import numpy as np
import scipy.sparse as sp

def boundary(a,b):
    """
    creates the boundary matrix from a to b, given as lists of strings,
    which is the coefficient of the 
    boundary functions: d_i(e_sigma) = sum((-1)**(index(i))e_sigma\i,i)
    """
    numRow = len(b)
    numCol = len(a)
    # make a a list of lists and b a dictionary with faces as keys and 
    # index in b as values
    a = map(lambda s: s.split(','),a)
    b = {tuple(e): i
         for i, e in enumerate(map(lambda s: s.split(','),b))}
    if numRow ==0:
        B = sp.lil_matrix(np.ones((1,numCol)),dtype=np.int8)
    else:
        # make matrix
        B = sp.lil_matrix((numRow,numCol),dtype =np.int8)
        # insert 1's and -1's for the boundary
        for j in xrange(numCol):
            for i in xrange(len(a[j])):
                # figure out the e_sigma\i
                if i == 0:
                    tempStr = a[j][i+1:]
                elif i == len(a[j]):
                    tempStr = a[j][0:i]
                else:
                    tempStr = a[j][0:i]+a[j][i+1:]
                try:
                    # find e_sigma\j in b and calculate the sign for it
                    temp = b[tuple(tempStr)]
                    B[temp,j]=(-1)**i
                except ValueError:
                    raise ValueError('inputs does not match: a=%s , b=%s' 
                        %(' '.join(map(str,a)), ' '.join(map(str,b))))
    return B
