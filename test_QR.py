#Homework 5
#test_QR.py file

import QR
import pytest


#Test Inputs
vector_11 = [1, 0, 0]
vector_12 = [1, 1, 1]

vector_21 = [1, 0]
vector_22 = [0, 1]
vector_23 = [1, 2]
vector_24 = [3, 4]

matrix_31 = [[1, 0], [0, 1]]
matrix_32 = [[1, 0], [1, 2]]
matrix_33 = [[[1.0, 0.0], [0.0, 1.0]], [[1.0, 0], [0, 1.0]]]
matrix_34 = [[[1.0, 0.0], [0.0, 1.0]], [[1.0, 0], [1, 2.0]]]

matrix_41 = [[1, 0], [0, 1]]
matrix_42 = [[1, 0], [3, 4]]
matrix_43 = [[[1.0, 0.0], [0.0, 1.0]], [[1.0, 0], [0, 1.0]]]
matrix_44 = [[[1.0, 0.0], [0.0, 1.0]], [[1.0, 0], [3, 4.0]]]


def test_normalize():
    assert QR.normalize(vector_11) == [[1.0, 0.0, 0.0], 1.0]
    assert QR.normalize(vector_12) == [[1/3**.5, 1/3**.5, 1/3**.5], 3**.5]
    #Result is infinite decimal.

def test_orthagonalize():
    #Test for Identity.
    assert QR.orthagonalize(vector_21, vector_22) == [[1, 0], 0]
    assert QR.orthagonalize(vector_23, vector_24) == [[-32, -42], 11]

def test_unstable_gram_schmidt():
    #Test for Identity.
    assert QR.unstable_gram_schmidt(matrix_31) == matrix_33
    assert QR.unstable_gram_schmidt(matrix_32) == matrix_34

def test_stable_gram_schmidt():
    #Test for Identity.
    assert QR.stable_gram_schmidt(matrix_41) == matrix_43
    assert QR.stable_gram_schmidt(matrix_42) == matrix_44

if __name__ == '__main__':
    pytest.main(['test_QR.py'])

