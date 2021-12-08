#Final Project
import LA
import QR
import LS


print('Hi, my name is Chase Stearns and I am the author of this Linear Algebra library.')
print(' ')

print('This library contains 3 scripts: LA.py, QR.py, and LS.py which contain and perform various linear alegrba functions.')
print(' ')

print('This section covers the first script. LA.py contains a large number of functions for performing basic linear algebra tasks.')
print(' ')

print('The 1st function in LA.py is add_vectors. It will take in two vectors as its arguments and return their sum.')
print('For example, if V1 = [1, 2] and V2 = [3, 4], then add_vectors(V1, V2) will return')
V1 = [1, 2]
V2 = [3, 4]
print(LA.add_vectors(V1, V2))
print(' ')

print('The 2nd function in LA.py is sca_vec_mult. It will take in a scalar and vector as its arguments and return their product.')
print('For example, if S1 = 3 and V3 = [3, 4], then sca_vec_mult(S1, V3) will return')
S1 = 3
V3 = [1, 2, 3]
print(LA.sca_vec_mult(S1, V3))
print(' ')

print('The 3nd function in LA.py is sca_mat_mult. It will take in a scalar and matrix as its arguments and return their product.')
print('For example, if S2 = 3 and M1 = [[1, 2], [3, 4]], then sca_mat_mult(S2, M1) will return')
S2 = 3
M1 = [[1, 2], [3, 4]]
print(LA.sca_mat_mult(S2, M1))
print(' ')

print('The 4th function in LA.py is mat_add. It will take in two matrices as its arguments and return their sum.')
print('For example, if M2 = [[1, 2], [3, 4]] and M3 = [[5, 6], [7, 8]], then mat_add(M2, M3) will return')
M2 = [[1, 2], [3, 4]]
M3 = [[5, 6], [7, 8]]
print(LA.mat_add(M2, M3))
print(' ')

print('The 5th function in LA.py is mat_vec_mult. It will take in a vector and a matrix as its agruments and return their product.')
print('For example, if V4 = [5, 6] and M4 = [[1, 2], [3, 4]], then mat_vec_mult(M4, V4) will return')
V4 = [5, 6]
M4 = [[1, 2], [3, 4]]
print(LA.mat_vec_mult(M4, V4))
print(' ')

print('The 6th function in LA.py is mat_mult. It will take in two matrices as its agruments and return their product.')
print('For example, if M5 = [[1, 2], [3, 4]] and M6 = [[5, 6], [7, 8]], then mat_mult(M5, M6) will return')
M5 = [[1, 2], [3, 4]]
M6 = [[5, 6], [7, 8]]
print(LA.mat_mult(M5, M6))
print(' ')

print('The 7th function in LA.py is complex_conjugate. It will take in a complex number as its agrument and return the complex conjuagte.')
print('For example, if CN1 = (-3.1+2.4j), then complex_conjuagte(CN1) will return')
CN1 = (-3.1+2.4j)
print(LA.complex_conjugate(CN1))
print(' ')

print('The 8th function in LA.py is absolute_value. It will take in a scalar/complex number as its agrument and return the absolute value.')
print('For example, if N1 = -4.6, then absolute_value(N1) will return')
N1 = -4.6
print(LA.absolute_value(N1))
print('For example, if CN2 = (4-3j), then absolute_value(CN2) will return')
CN2 = (4-3j)
print(LA.absolute_value(CN2))
print(' ')

print('The 9th function in LA.py is finite_p_norm. It will take in a vector and p(if not given a p it will default to p=2) as its agruments and return the p-norm.')
print('For example, if V5 = [3, 4], then finite_p_norm(V5) will return')
V5 = [3, 4]
print(LA.finite_p_norm(V5))
print('For example, if V6 = [3, 4] and p=1, then finite_p_norm(V6, p=1) will return')
V6 = [5, (3+4j)]
print(LA.finite_p_norm(V6, p=1))
print(' ')

print('The 10th function in LA.py is infinite_p_norm. It will take in a vector as its agrument and return the infinite p-norm.')
print('For example, if V7 = [3, 4], then infinite_p_norm(V7) will return')
V7 = [3, 4]
print(LA.infinite_p_norm(V7))
print('For example, if V8 = [3, (3+4j)], then infinite_p_norm(V8) will return')
V8 = [3, (3+4j)]
print(LA.infinite_p_norm(V8))
print(' ')

print('The 11th function in LA.py is p_norm. It will take in a vector as its agrument and return the p-norm or infinity p-norm depending on if infifnity it True.')
print('For example, if V9 = [3, 4], then p_norm(V9) will return')
V9 = [3, 4]
print(LA.p_norm(V9))
print('For example, if V10 = [3, 4], then p_norm(V10,infinity = True) will return')
V10 = [3, (3+4j)]
print(LA.p_norm(V10,infinity=True))
print(' ')

print('The 12th function in LA.py is inner_product. It will take in two vectors as its arguments and return their inner product.')
print('For example, if V11 = [7, -8, 9] and V12 = [(1+2j), (3+4j), (5-6j)], then inner_product(V11, V12) will return')
V11 = [7, -8, 9]
V12 = [(1+2j), (3+4j), (5-6j)]
print(LA.inner_product(V11, V12))
print(' ')

print('END of LA.py')
print(' ')
print(' ')


print('This section covers the second script. QR.py contains various approaches for QR Factorization.')
print(' ')

print('The 1st function in QR.py is normalize. It will take in a vector as its argument and return the normalized vector and norm of the vector.')
print('For example, if V13 = [1, 0, 0], then normalize(V13) will return')
V13 = [1, 0, 0]
print(QR.normalize(V13))
print(' ')

print('The 2nd function in QR.py is orthagonalize. It will take in a vector and a basis(as a vector) as its arguments and return the orthagonalized vector and the inner product of the vector and basis vector.')
print('For example, if V14 = [1, 2] and V15 = [3, 4], then orthagonalize(V14, V15) will return')
V14 = [1, 2]
V15 = [3, 4]
print(QR.orthagonalize(V14, V15))
print(' ')

print('The 3rd function in QR.py is stable_gram_schmidt. It will take in a matrix as its argument and return the orthonormal matrix, Q of the input matrix and the upper triangular matrix, R of the input matrix.')
print('For example, if M7 = [[1, 0], [3, 4]], then stable_gram_schmidt(M7) will return')
M7 = [[1, 0], [3, 4]]
print(QR.stable_gram_schmidt(M7))
print(' ')

print('The 4th function in QR.py is orthonormal. It will take in a matrix as its argument and return the orthonormal matrix with the same span as the input matrix.')
print('For example, if M8 = [[1, 0], [3, -4]], then orthonormal(M8) will return')
M8 = [[1, 0], [3, -4]]
print(QR.orthonormal(M8))
print(' ')

print('The last function in QR.py is QR_Householder. It will take in a matrix as its argument and return the orthonormal matrix with the same span as the input matrix.')
print('For example, if M9 = [[1,1,1], [-1,4,4], [4,-2,0]], then QR_Householder(M9) will return')
M9 = [[1,1,1], [-1,4,4], [4,-2,0]]
print(QR.QR_Householder(M9))
print(' ')

print('END of QR.py')
print(' ')
print(' ')


print('This section covers the third script. LS.py contains the function for least squares.')
print(' ')

print('The 1st function in LA.py is Least_Squares. It will take in a vector and matrix as its arguments and return the least squares solution.')
print('For example, if V16 = [0,1,0] and M10 = [[5,6,2], [3,7,8], [2,6,3]], then Least_Squares(V16, M10) will return')
V16 = [0,1,0]
M10 = [[5,6,2], [3,7,8], [2,6,3]]
print(LS.Least_Squares(V16, M10))
print(' ')

print('END of LS.py')

