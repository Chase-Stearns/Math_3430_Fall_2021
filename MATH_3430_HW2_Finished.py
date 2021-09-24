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
A3: We will create an empty list, called result and will store the scaled 
vector using append. The scalar will be multiplied by the corresponding
element of the vector.
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
    result = []
    for element in vector:
        result.append(element * scalar)
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
A3: We will create an empty list, called result and will store the scaled 
matrix using append. The scalar will be multiplied by the corresponding
vector of the matrix.

algorithm nam: sca_mat_mult(scalar,matrix)

initialize result as a copy of matrix, named result.

For each list in result, replace the list with the output of
sca_vec_mult(scalar,vector)

return result
"""
def sca_mat_mult(scalar,matrix):
    result = []
    for vector in matrix:
        result.append(sca_vec_mult(scalar,vector))
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
represents a column. We call these matrices matrix_A and matrix_B.
    
Q2: What do we want?
A2: The sum of matrix_A and matrix_B stored as a list of lists, where each
component list represents a column.
    
Q3: How will we get there?
A3: We will create en empty list, called result and the use append to get the 
sum of the corresponding vectors in matrix_A and matrix_B.

algorithm name: mat_add(matrix_A,matrix_B)

initialize result as an empty list.

For each list in result, replace it with add_vectors(list, coressponding list
from matrix_B)

return result                
"""
def mat_add(matrix_A,matrix_B):
    result = []
    for index in range(len(matrix_A)):
        result.append(add_vectors(matrix_A[index],matrix_B[index]))
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
A3: We will creat an empty list, called result. Then by linear combination we 
will multiply each column of the matrix by the corresponding element of the 
vector, then we will sum all the resulting vectors and return the final 
resultant vector.

algorithm name: mat_vec(matrix,vector)

initialize result vector of 0's, same length as the first list in matrix, call
it result.

for each list in matrix, overwrite it as the result from
sca_vec_mult(corresponding element of vector, list)

for each list in matrix, set result = result + list,

return result 
"""

def mat_vec_mult(matrix,vector):
    result = []
    for element in matrix[0]:
        result.append(0)
    vectors = []
    for index in range(len(vector)):
        vectors.append(sca_vec_mult(vector[index],matrix[index]))
    for single_vector in vectors:
        result = add_vectors(result,single_vector)
        
    return result


#Test Inputs 04
test_matrix_41 = [[1, 2], [3, 4]]
test_matrix_42 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_vector_41 = [5, 6]
test_vector_42 = [10, 11, 12]

# mat_vec_mult(test_matrix_41,test_vector_41) should output [23, 34]
print('Test Output for mat_vec_mult: ' + str(mat_vec_mult(test_matrix_41,test_vector_41)))
print('Should have been [23, 34]')
# mat_vec_mult(test_matrix_42,test_vector_42) should output [138, 171, 204]
print('Test Output for mat_vec_mult: ' + str(mat_vec_mult(test_matrix_42,test_vector_42)))
print('Should have been [138, 171, 204]')

#End Problem 04

"""
Problem 05
Q1: What do we have?
A1: Two matrices, stored as lists of lists, where each component list represents
a column. We call these matrices matrix_A and matrix_B.
    
Q2: What do we want?
A2: The product matrix_A * matrix_B.
    
Q3: How will we get there?
A3: We will create an empty list, called result. Then by linear combination 
of the corresponding column used in mat_vec_mult we will then use append to 
return the resultant matrix.
    
algorithm name: mat_mult

Initialize result as an empty list.

for column in result, set column = mat_vec_mult(matrix_B,column)

return result
"""

def mat_mult(matrix_A,matrix_B):
    result = []
    for column in matrix_B:
        result.append(mat_vec_mult(matrix_B,column))
    return result

#Test Outputs
test_matrix_51 = [[1, 2], [3, 4]]
test_matrix_52 = [[5, 6], [7, 8]]
test_matrix_53 = [[5, 6,], [7, 8], [9, 10]]

# mat_mult(test_matrix_51,test_vector_52) should output [[67, 78], [91, 106]]
print('Test Output for mat_mult: ' + str(mat_mult(test_matrix_51,test_matrix_52)))
print('Should have been [[67, 78], [91, 106]]')
# mat_vec_mult(test_matrix_51,test_vector_53) should output [[67, 78], [91, 106], [115, 134]]
print('Test Output for mat_mult: ' + str(mat_mult(test_matrix_51,test_matrix_53)))
print('Should have been [[67, 78], [91, 106], [115, 134]]')

#End Problem 05

