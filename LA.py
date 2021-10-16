#Homework #03


# Begin Example
# Problem #0
def add_vectors(vector_a: list,
                vector_b: list) -> list:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result
# End Example

#Problem #01
def sca_vec_mult(scalar: float,vector: list) -> list:
    '''Multiplies the input scalar by the input vector.
    
    Creates an empty list, called result. The scalar is multiplied to the
    corresponding element of the vector and is appended to the empty list and
    returned.
    
    Arguments:
        scalar: A scalar stored as a float.
        vector: A vector stored as a list.
        
    Returns:
        The product of the input scalar and the vector, stored as a list.
    '''
    result: list = []
    for element in vector:
        result.append(element * scalar)
    return result

#Problem #02
def sca_mat_mult(scalar: float,matrix: list) -> list:
    '''Multiplies the input scalar by the input matrix.
    
    Creates an empty list, called result. The scalar is multiplied to the
    corresponding element of the corrseponding vector (or list) using 
    sca_vec_mult of the matrix (list of lists) and is appended to the empty
    list and returned.
    
    Arguments:
        scalar: A scalar stroed as a float.
        matrix: A matrix stored as a list of lists.
        
    Returns:
        The product of the input scalar and the matrix, stored as a list of lists..
    '''
    result: list = []
    for vector in matrix:
        result.append(sca_vec_mult(scalar,vector))
    return result

#Problem #03
def mat_add(matrix_A: list,matrix_B: list) -> list:
    '''Adds the input matrix_A and input matrix_B.
    
    Creates an empty list, called result. The vectors (or lists) of matrix_A
    are added to the corresponding vectors (or lists) of matrix_b using
    add_vectors and is appended to the empty list and returned.
    
    Arguments:
        matrix_A: A matrix stored as a list of lists.
        matrix_B: A matrix that has the same length as matrix_A, stored as a
        list of lists.
        
    Returns:
        The sum of the input matrix_A and the input matrix_B, stored as a list
        of lists.
    '''
    result: list = []
    for index in range(len(matrix_A)):
        result.append(add_vectors(matrix_A[index],matrix_B[index]))
    return result

#Problem #04
def mat_vec_mult(matrix: list,vector: list) -> list: 
    '''Multiplies the input vector by the input matrix.
    
    Creates an empty list, called result. The elements of the vector (or list)
    multiplied by the corresponding vector (or list) of the matrix using
    sca_vec_mult. Then using add_vectors adding the lists to the empty list.
    
    Arguments:
        matrix: A matrix stored as a list of lists.
        vector: A vector that has the same length as the matrix, stored as a
        list.
        
        
    Returns:
        The product of the input vector and the input matrix, stored as a list
        of lists.
    '''
    result: list = []
    for element in matrix[0]:
        result.append(0)
    lists: list = []
    for index in range(len(vector)):
        lists.append(sca_vec_mult(vector[index],matrix[index]))
    for column in lists:
        result = add_vectors(result,column)
        
    return result

#Problem #05
def mat_mult(matrix_A: list,matrix_B: list) -> list:
    '''Multiplies the input matrix_A by the input matrix_B.
    
    Creates an empty list, called result. Using mat_vec_mult each vector 
    (or list) of matrix_A in order will be multiplied by each corresponding
    vector (or list) of matrix_B. Then the product matrix is appended to result
    and returned.
    
    Arguments:
        matrix_A:
        matrix_B:
        
    Returns:
        The product of the input matrix_A and the input matrix_B, stored as a 
        list of lists.
    '''
    result: list = []
    for column in matrix_B:
        result.append(mat_vec_mult(matrix_B,column))
    return result
