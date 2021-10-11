#Homework 02

#Example:
#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#Test Inputs 00
test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [1, 5, 9]

# add_vectors(test_vector_01,test_vector_02) should output [4 ,3, 6]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4, 3, 6]')

# add_vectors(test_vector_02,test_vector_03) should output [4, 6, 11]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_02,test_vector_03)))
print('Should have been [4, 6, 11]')

#End Example

"""
Problem 01
Q1: What do we have?
A1: A scalar, called scalar, and a vector stored as a list, called vector.

Q2: What do we want?
A2: The scaled vector which result from multiplying vector by scalar.

Q3: How will we get there?
A3: We will create a result vector, called result, containing the same elements as vector.
Then multiply each element of result, by scalar.
"""
"""
def scalar_vec_multi(scalar,vector):
    for element in vector:
        element *= scalar
    return vector

algorithm name: scalar_vec_multi(scalr,vector)

Initializing result as a copy of vector.

For each element in result, multiply it by scalar.

return result
"""
def sca_vec_mult(scalar,vector):
    result = vector
    for index in range(len(result)):
        result[index] *= scalar
    return result

#Test Inputs 01
test_vector_11 = [1, 2, 3]
test_vector_12 = [3, 1, 2]
test_scalar_11 = 2
test_scalar_12 = 3

# sca_vec_mult(test_scalar_11,test_vector_11) should output [2, 4, 6]
print('Test Output for sca_vec_mult: ' + str(sca_vec_mult(test_scalar_11,test_vector_11)))
print('Should have been [2, 4, 6]')
# sca_vec_mult(test_scalar_12,test_vector_12) should output [9, 3, 6]
print('Test Output for sca_vec_mult: ' + str(sca_vec_mult(test_scalar_12,test_vector_12)))
print('Should have been [9, 3, 6]')

#End Problem 01

"""
Problem 02
Q1: What do we have?
A1: A scalar, called scalar, and a matrix stored as a list of lists, called
matrix. Each list in matrix represents a column vector.
    
Q2: What do we want?
A2: We want the matrix which is the scaled version of the given matrix.
    
Q3: How will we get there?
A3: We will cpoy matrix into a result matrix. Then we will use
sca_vec_mult on each of the column vectors now stored in result.

algorithm nam: sca_mat_mult(scalar,matrix)

initialize result as a copy of matrix, named result.

For each list in result, replace the list with the output of
sca_vec_mult(scalar,vector)

return result
"""
def sca_mat_mult(scalar,matrix):
    result = matrix
    for columns in range(len(matrix)):
        for rows in range(len(matrix[0])):
            result[columns][rows] *= scalar
            
    return result

#Test Inputs 02
test_matrix_21 = [[1, 2], [3, 4]]
test_matrix_22 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_scalar_21 = 3
test_scalar_22 = 4

# sca_mat_mult(test_scalar_21,test_matrix_21) should output [[3, 6], [9, 12]]
print('Test Output for sca_mat_mult: ' + str(sca_mat_mult(test_scalar_21,test_matrix_21)))
print('Should have been [[3, 6], [9, 12]]')
# sca_mat_mult(test_scalar_22,test_mtarix_22) should output [[4, 8, 12], [16, 20, 24], [28, 32, 36]]
print('Test Output for sca_mat_mult: ' + str(sca_mat_mult(test_scalar_22,test_matrix_22)))
print('Should have been [[4, 8, 12], [16, 20, 24], [28, 32, 36]]')

#End Problem 02

"""
Problem 03
Q1: What do we have?
A1: We have two matrices stored as lists of lists, where each component list
represents a column. We call these matrices matrix_a and matrix_b.
    
Q2: What do we want?
A2: The sum of matrix_a and matrix_b stored as a list of lists, where each
component list represents a column.
    
Q3: How will we get there?
A3:We will initialize a result matrix as a copy of matrix_a. Then for each list
in result, we will add the corresponding list from matrix_b, using add_vectors.

algorithm name: mat_add(matrix_a,matrix_b)

initialize result as a copy of matrix_a.

For each list in result, replace it with add_vectors(list, coressponding list
from matrix_B)

return result                
"""
def mat_add(matrix_a,matrix_b):
    result = matrix_a
    for columns in range(len(matrix_a)):
        for rows in range(len(matrix_a[0])):
            result[columns][rows] += matrix_b[columns][rows]
            
    return result

#Test Inputs 03
test_matrix_31 = [[1, 2], [3, 4]]
test_matrix_32 = [[5, 6], [7, 8]]
test_matrix_33 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_matrix_34 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

# mat_add(test_matrix_31,test_matrix_32) should output [[6, 8], [10, 12]]
print('Test Output for mat_add: ' + str(mat_add(test_matrix_31,test_matrix_32)))
print('Should have been [[6, 8], [10, 12]]')
# mat_add(test_matrix_33,test_matrix_34) should output [[11, 13, 15], [17, 19, 21], [23, 25, 27]]
print('Test Output for mat_add: ' + str(mat_add(test_matrix_33,test_matrix_34)))
print('Should have been [[11, 13, 15], [17, 19, 21], [23, 25, 27]]')

#End Problem 03

"""
Problem 04
Q1: What do we have?
A1: A matrix, called matrix, stroed as a list of lists, where each component
list represents a column of the matrix, and a vector, called vector, stored as
a list.
    
Q2: What do we want?
A2: The mtarix-vector multiplication of matrix and vector stored as a list.
    
Q3: How will we get there?
A3: We will create a result vector of 0's, which is the same size as a column
of the input matrix. We will then multiply each column of the matrix by the 
corresponding element of the vetor. Then we will add each of these scaled 
columns to result.

algorithm name: mat_vec(matrix,vector)

initialize result vector of 0's, same length as the first list in matrix, call
it result.

for each list in matrix, overwrite it as the result from
scalar_vec_multi(corresponding element of vector, list)

for each list in matrix, set result = result + list,

return result 
"""

#def mat_vec_mult(matrix,vector)

"""
Problem 05
Q1: What do we have?
A1: Two matrices, stored as lists of lists, where each component list represents
a column. We call these matrices matrix_A and matrix_B.
    
Q2: What do we want?
A2: The product matrix_A * matrix_B.
    
Q3: How will we get there?
A3: We will initialize a result matrix which is a copy of matrix_B, called
result. Then for each component of result, we will overwrite it with the output
of mat_vec(matrix_A, component).
    
algorithm name

Initialize result as a copy of matrix_B.

for column in result, set column = mat_vec(matrix_A,column)

return result
"""
