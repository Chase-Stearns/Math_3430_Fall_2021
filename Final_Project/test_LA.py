'''
Tests the functions in LA.py for HW #03 and #04
'''

import LA
import pytest

#Test inputs for HW #03

#Test Inputs 00
test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [1, 5, 9]

#Test Inputs 01
test_vector_11 = [1, 2, 3]
test_vector_12 = [3, 1, 2]
test_scalar_11 = 2
test_scalar_12 = 3

#Test Inputs 02
test_matrix_21 = [[1, 2], [3, 4]]
test_matrix_22 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_scalar_21 = 3
test_scalar_22 = 4

#Test Inputs 03
test_matrix_31 = [[1, 2], [3, 4]]
test_matrix_32 = [[5, 6], [7, 8]]
test_matrix_33 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_matrix_34 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

#Test Inputs 04
test_matrix_41 = [[1, 2], [3, 4]]
test_matrix_42 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_vector_41 = [5, 6]
test_vector_42 = [10, 11, 12]

#Test Inputs 05
test_matrix_51 = [[1, 2], [3, 4]]
test_matrix_52 = [[5, 6], [7, 8]]
test_matrix_53 = [[5, 6,], [7, 8], [9, 10]]

def test_add_vectors():
    #result_01 = [1+2, 2+1, 4+2]
    result_01 = [4, 3, 6]
    assert LA.add_vectors(test_vector_01,test_vector_02) == result_01
    #result_02 = [3+1, 1+5, 2+9]
    result_02 = [4, 6, 11]
    assert LA.add_vectors(test_vector_02,test_vector_03) == result_02
    
def test_sca_vec_mult():
    #result_11 = [2*1, 2*2, 2*3]
    result_11 = [2, 4, 6]
    assert LA.sca_vec_mult(test_scalar_11,test_vector_11) == result_11
    #result_12 =[3*3, 3*1, 3*2]
    result_12 = [9, 3, 6]
    assert LA.sca_vec_mult(test_scalar_12,test_vector_12) == result_12
    
def test_sca_mat_mult():
    #result_21 = [[3* 1, 3*2], [3*3, 3*4]]
    result_21 = [[3, 6], [9, 12]]
    assert LA.sca_mat_mult(test_scalar_21,test_matrix_21) == result_21
    #result_22 = [[4*1, 4*4, 4*3], [4*4, 4*5, 4*6], [4*7, 4*8, 4*9]]
    result_22 = [[4, 8, 12], [16, 20, 24], [28, 32, 36]]
    assert LA.sca_mat_mult(test_scalar_22,test_matrix_22) == result_22
    
def test_mat_add():
    #result_31 = [[1+5, 2+6], [3+7, 4+8]]
    result_31 = [[6, 8], [10, 12]]
    assert LA.mat_add(test_matrix_31,test_matrix_32) == result_31
    #result_32 = [[1+10, 2+11, 3+12], [4+13, 5+14, 6+15], [7+16, 8+17, 9+18]]
    result_32 = [[11, 13, 15], [17, 19, 21], [23, 25, 27]]
    assert LA.mat_add(test_matrix_33,test_matrix_34) == result_32
    
def test_mat_vec_mult():
    #result_41 = [[1*5 + 3*6], [2*5 + 4*6]]
    result_41 = [23, 34]
    assert LA.mat_vec_mult(test_matrix_41,test_vector_41) == result_41
    #result_42 =[[1*10 + 4*11 + 7*12], [2*10 + 5*11 + 8*12], [3*10 + 6*11 + 9*12]]
    result_42 = [138, 171, 204]
    assert LA.mat_vec_mult(test_matrix_42,test_vector_42) == result_42
    
def test_mat_mult():
    result_51 = [[67, 78], [91, 106]]
    assert LA.mat_mult(test_matrix_51,test_matrix_52) == result_51
    result_52 = [[67, 78], [91, 106], [115, 134]]
    assert LA.mat_mult(test_matrix_51,test_matrix_53) == result_52

#Homework 04

def test_complex_conjugate():
    #Test for zero.
    assert LA.complex_conjugate(0) == 0j
    #Test for positive integer.
    assert LA.complex_conjugate(2) == (2+0j)
    #Test for negative integer.
    assert LA.complex_conjugate(-3) == (-3+0j)
    #Test for positive float.
    assert LA.complex_conjugate(2.7) == (2.7-0j)
    #Test for negative float.
    assert LA.complex_conjugate(-4.6) == (-4.6-0j)
    #Test for complex integer.
    assert LA.complex_conjugate(complex(2,-3)) == (2+3j)
    #Test for complex float.
    assert LA.complex_conjugate(complex(-3.1,2.4)) == (-3.1-2.4j)

def test_absolute_value():
    #Test for zero.
    assert LA.absolute_value(0) == 0.0
    #Test for positive integer.
    assert LA.absolute_value(2) == 2.0
    #Test for negative integer.
    assert LA.absolute_value(-3) == 3.0
    #Test for positive float.
    assert LA.absolute_value(2.7) == 2.7
    #Test for negative float.
    assert LA.absolute_value(-4.6) == 4.6
    #Test for complex integer.
    assert LA.absolute_value(complex(4,-3)) == 5.0

def test_finite_p_norm():
    #Test for vector with real numbers.
    assert LA.finite_p_norm([3, 4]) == 5.0
    #Test for vector with complex numbers.
    assert LA.finite_p_norm([5, complex(3, 4)], p=1) == 10.0
    
def test_infinite_p_norm():
    #Test for vector with real numbers.
    assert LA.infinite_p_norm([3, 4]) == 4.0
    # Test for vector with complex numbers.
    assert LA.infinite_p_norm([3, complex(3, 4)]) == 5.0

def test_p_norm():
    #Test for vector with real numbers.
    assert LA.p_norm([3, 4]) == 5.0
    #Test for vector with complex numbers.
    assert LA.p_norm([5, complex(3,4)], p=1) == 10.0
    #Test for vector with real numbers.
    assert LA.p_norm([3, 4],infinity = True) == 4.0
    #Test for vector with complex numbers.
    assert LA.p_norm([3, complex(3,4)],infinity = True) == 5.0

vector_1 = [1, 2, 3]
vector_2 = [4, -5, 6]
vector_3 = [7, -8, 9]
complex_vector = [complex(1,2), complex(3,4), complex(5,-6)]

def test_inner_product():
    #Test for vectors with real numbers.
    assert LA.inner_product(vector_1,vector_2) == (12+0j)
    #Test for vectors with real and complex numbers.
    assert LA.inner_product(vector_3,complex_vector) == (28-72j)
    #Test for vectors with real and complex numbers.
    assert LA.inner_product(complex_vector,vector_3) == (28-72j)


if __name__ == '__main__':
    pytest.main(['test_LA.py'])
