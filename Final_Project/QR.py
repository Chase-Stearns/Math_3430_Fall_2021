import LA

def normalize(vector: list) -> list:
    '''Normalizes the input vector. The norm of the input vector is found using
    p_norm. Then the input vector is then multiplied by 1/norm. The result and 
    norm are then returned.

    Arguments:
        vector: A vector stored as a list contanining real/complex numbers.

    Returns:
        The normalized input vector and norm of the input vector.
    '''
    norm: float = LA.p_norm(vector)
    result: list = LA.sca_vec_mult(1/norm,vector)

    return [result,norm]


def orthagonalize(vector: list, basis: list) -> list:
    '''Orthagonalizes the input vector rejection of input vector on input basis
    vector. Using inner_product the inner product of the input vector and input
    basis and stored as product. The product is then used as a scalar to find 
    the negated vector projection of the input vector on the input basis using
    sca_vec_mult and subtracted from the input vector, stored as 
    negated_projection. Then using add_vectors add the input vector and the 
    negated_projection, stored as result. The result and product is returned.

    Arguments:
        vector: A vector stored as a list.
        basis: A second vector stored as a list.
    Returns:
        The orthagonalized input vector and the inner product of the input
        vector and input basis vector.
    '''
    product: complex = LA.inner_product(vector,basis)
    negated_projection: list[complex] = LA.sca_vec_mult(-1*product,basis)
    result: list[complex] = LA.add_vectors(vector,negated_projection)

    return [result,product]

def stable_gram_schmidt(matrix: list) -> list:
    '''Uses the Modified Gram-Schmidt formula to find the reduced QR 
    factorization of the input matrix.
    First, initialize matrix Q to be a copy of the input matrix and matrix R to
    be a 0 matrix. Then, iterate over every column vector in matrix Q. 
    Normalize the vector and store the normalization in matrix R. Then, 
    orthagonalize every following vector in matrix Q corresponding to the current
    column that is being evaluated, stored as matrix R. Returning the matrices 
    Q and R.
    Arguments:
        matrix: A matrix stored as a list of lists.
    Returns:
        The orthonormal matrix, Q of the input matrix and the upper triangular 
        matrix, R fo the input matrix.
    '''
    Q: list = [column[:] for column in matrix]
    R: list = [[0 for m in matrix] for n in matrix]
    
    for element, vector in enumerate(Q):
        normalize_operation = normalize(vector)
        Q[element] = normalize_operation[0]
        R[element][element] = normalize_operation[1]
        for index, orthagonal_vector in enumerate(Q[element+1:],start=element+1):
            orthagonal_operation = orthagonalize(orthagonal_vector,vector)
            Q[index] = orthagonal_operation[0]
            R[index][element] = orthagonal_operation[1]

    return [Q,R]

def orthonormal(matrix: list) -> list:
    """Finds the orthonormal list of vectors(or lists) of the input matrix. 
    Uses stable_gram_schmidt and returns Q of the QR factorization and stored
    as a list of vectors(or lists) in result. The result is then returned.
    Arguments:
        matrix: A matrix stored as a list of vectors(or lists).
    Returns:
        An orthonormal matrix with the same span as the input matrix.
    """
    result: list = stable_gram_schmidt(matrix)[0]
    return result

def Identity_Matrix(n: int)-> int: 
    """Computes the identity matrix.
    First we set each element in the matrix, n equal to zero, then we replace 
    each zero of the input, n with a one for the corresponding diagonal values.
    
    Arguments:
        matrix_a: A matrix stored as a list of lists
    
    Returns:
        The identity of the input matrix.
    """
    result: list = [[0 for element in range(n)] for index in range(n)]
    for index in range(n):
        result[index][index] = 1
    return result

def sign(n: float)-> float:
    '''Determines the sign of a number or whether a number is positive or 
    negative.
    The input number, n is less than zero, the function returns -1 and if the
    input number, n is greater than zero, the function returns 1.
    
    Arguments:
        n: An number as a float.
    Returns:
        The sign of the input number. 
    '''
    if n < 0:
        return -1
    else:
        return 1

def conjugate_transpose(matrix: list)-> list:
    '''Computes the conjugate transpose of the input matrix.
    1st creating two resultant matricies as copies of the input matrix of same 
    nxm size filled with 0's. Implement a two for loops to make the rows and 
    columns of the first resultant matrix to be the conjugate transpose of the
    matrix. Finally using the same process, implement the same technique for 
    the second resultant matrix to be equal to the conjugated matrix. The 
    second resultant matrix will then be returned.
    
    Arguments: 
        matrix: A matrix stored as a list of lists.
    Returns:
        The conjugated transpose of the input matrix.    
    '''
    result_1:list = [[0 for element in range(len(matrix))] for i in range(len(matrix[0]))]
    for index_1 in range(len(matrix[0])):
        for index_2 in range(len(matrix)):
            result_1[index_1][index_2] = LA.complex_conjugate(matrix[index_2][index_1])
    return result_1

def V_Calculate(vector: list)-> list:
    '''Calculates the reflection of the input vector.
    1st find the reflection vector, V which V must satisfy the equation 
    V = sign(x)||x||e + x, and e is a vector with the first element being 1 and
    the others 0 ([1,0,0...n]). Finally returning the result, V.
    
    Arguments:
        vector: A vector stored as a list.
    
    Returns:
        The reflection vector, V of the input vector.
    
    '''
    e: list = [0 for element in vector]
    e[0] = 1
    vnorm: list = LA.p_norm(vector)
    s:list = sign(vector[0]) * vnorm
    w:list =LA.sca_vec_mult(s, e)
    V:list = LA.add_vectors(w, vector)
    return V

def vec_mult(vector:list, vector_b:list)-> list:
    '''Calculates the product of the two input vectors.
    1st we set our result as an empty list. Next, we create the first for loop
    to go through each element in our first input vector and use sca_vec_mult
    to multiply that to the elements of the second input vector and append the 
    resulting values to the empty list and return the result.
    
    Arguments: 
        vector: A vector stored as a list.
        vector_b: A vector stored as a list.
    
    Returns:
        The product of two input vectors.   
    '''
    result: list = []
    for index in range(len(vector)):
        result.append(LA.sca_vec_mult(vector[index], vector_b))
    return result

def F_Calculate(Vector: list) -> list:
    '''Calculates F_k matrix in the equation F_k = I - 2(vv*/v*v) which will be
    used to compute Q.
    First we let a scalar, h, that equals -2 divided by the value of the p-norm
    of our vector squared. Next, we take the product of our previous two 
    vectors and use sca_vec_mult to multiply it times h and set that new matrix
    equal to i. Finally, we use mat_add to add what we got from Identity_Matrix
    to our and return the result.
    
    Arguments:
        Vector: A vector stored as a list.
    Returns:
        The F_k matrix that is used to calculate Q.
    '''
    h = -2/(LA.p_norm(Vector))**2
    i = LA.sca_mat_mult(h, vec_mult(Vector, Vector))
    F = LA.mat_add(Identity_Matrix(len(Vector)), i)
    return F 


def deep_copy(matrix: list) -> list: 
    '''Produces a deep copy of the input matrix.
    1st initialize the result matrix of the input matrix of same nxn size. The
    elements of the resultant matrix will be set to zero. Then, the the rows 
    and columns will become a copy of the desired matrix to be copied. Finally,
    the result will be returned.
    
    Arguments:
        matrix: A matrix stored as a list of lists.
    
    Returns:
        The deep copy of the input matrix.
    '''
    result: list = [[0 for element in range(len(matrix[0]))] for i in range(len(matrix))]
    for index_1 in range(len(matrix)):
        for index_2 in range(len(matrix)):
            result[index_1][index_2] = matrix[index_1][index_2]
    return result


def Q_Calculate(matrix: list, k: float)-> list:
    ''' Calculates Q_k matrix which will be used to calculate the QR Householder 
    factorization.
    1st initialize the result matrix of the input matrix to be replaced with 
    0's. Q has to be in the form Q = [[I_k-1, 0], [0, F_k]], in order to do so,
    run a for loop to initialize the input matrix to be of the same dimensions
    of the matrix [[I_k-1, 0], [0, F_k]]. F_k is written, so we can set an 
    element f equal to F_k using F_Calculate. Using Identity_Matrix, set Q_k as
    Q_Calculate equal to the identity matrix. Then, adding the F_k value f into
    the Q matrix using for loops to put it in the correct a22 posistion. 
    Finally, returning the result.
    Arguments:
        matrix: A matrix stored as a list of lists.
        K: An integer representing the indexing iterations.
    Returns:
        The matrix Q_k that is used to calculate the QR Householder factorization.
    '''
    Q: list = [[0 for element in range(k, len(matrix[index]))] for index in range(k, len(matrix))]
    for index in range(len(matrix)):
        for element in range(len(matrix[index])):
            if k + index < len(matrix[index]):
                if k + element < len(matrix[index]):
                    Q[index][element] = matrix[k + index][k + element]
    v: list = V_Calculate(Q[0])
    f: list = F_Calculate(v)
    Q_Calculate = Identity_Matrix(len(matrix))
    for index in range(k, len(Q_Calculate)):
        for element in range(k, len(Q_Calculate)):
            Q_Calculate[index][element] = f[index - k][element - k]
    return Q_Calculate


def QR_Householder(matrix: list) -> list:
    '''Calculates the QR Householder factorization of the input matrix.
    1st, initializing R as the deep copy of the input matrix. Also, creating an
    empty list, Q_list. Then setting Q_temp, to be equal to the Q_k of R and 
    the indecies interating in the for loop. R then being set equal to the 
    multiplication of Q_temp * R. Use mat_mult to calculate R in QR 
    decomposistion. Next, append the values of Q_temp to Q_list, that is set to
    the final Q. Then, continuing with the last indecy for finish Q. Next, take
    the conjugate_transpose of Q_list beginning with the first vector. Lastly, 
    to finish building Q by taking the product of Q and the 
    conjugate_transpose. Finally, returning the result, Q and R.
    
    Arguments:
        matrix: A matrix stored as a list of lists.
    
    Returns:
        The resulting Q and R matrix of the QR Householder factorization.
    '''
    R: list = deep_copy(matrix)
    Q_list: list = []
    for index in range(len(R)):
        Q_temp: list = Q_Calculate(R, index)
        R = LA.mat_mult(Q_temp, R)
        Q_list.append(Q_temp)
    Q: list = Q_list[-1]
    Q: list = conjugate_transpose(Q_list[0])
    for index in range(1, len(Q_list)):
        Q = LA.mat_mult(Q, conjugate_transpose(Q_list[index]))
    return [Q, R]
