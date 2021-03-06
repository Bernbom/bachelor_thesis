import unittest
import numpy as np
import scipy.sparse as sp
import row

class TestRow(unittest.TestCase):

    def test_swap(self):
        A = np.matrix([[ -1, -1, -1, 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        A = sp.lil_matrix(A)
        row.swap(A,0,1)
        B = np.matrix([[ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ -1, -1, -1, 0, 0, 0, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        B = sp.lil_matrix(B)
        self.assertTrue((A-B).nnz==0)

    def test_scale(self):
        A = np.matrix([[ -1, -1, -1, 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        A = sp.lil_matrix(A)
        row.scale(A,0,float(-1))
        B = np.matrix([[ 1, 1, 1, 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        B = sp.lil_matrix(B)
        self.assertTrue((A-B).nnz==0)

    def test_scale_4(self):
        A = np.matrix([[ 4, 4, 4, 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        A = sp.lil_matrix(A)
        row.scale(A,0,1/float(4))
        B = np.matrix([[ 1, 1, 1, 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        B = sp.lil_matrix(B)
        self.assertTrue((A-B).nnz==0)        

    def test_combine(self):
        A = np.matrix([[ -1, -1, -1, 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        A = sp.lil_matrix(A)
        row.combine(A,0,1,1)
        B = np.matrix([[ 0, -1, -1, -1, -1, -1, 0, 0 ],
            [ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        B = sp.lil_matrix(B)
        self.assertTrue((A-B).nnz==0)

if __name__=='__main__':
    unittest.main()
