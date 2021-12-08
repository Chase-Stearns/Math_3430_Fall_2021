#test_LS.py file

import LA
import QR
import LS

import pytest

matrix_111 = [[5,6,2], [3,7,8], [2,6,3]]
matrix_112 = [[3,4,7], [2,9,6], [1,5,3]]
vector_111 = [0,1,0]
vector_112 = [1,4,2]
vector_113 = [(-1.2311901336207893e-09+0j), (9.441529873021763e-10+0j), 0j]
vector_114 = [(-1.6075817646771297e-10+0j), (1.627417634949895e-09+0j), (6.595299893826224e-09+0j)]

def test_Least_Squares():
    assert LS.Least_Squares(vector_111, matrix_111) == vector_113
    assert LS.Least_Squares(vector_112, matrix_112) == vector_114


if __name__ == '__main__':
    pytest.main(['test_LS.py'])

