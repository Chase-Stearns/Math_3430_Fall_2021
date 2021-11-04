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


def unstable_gram_schmidt(matrix: list) -> list:
    '''Uses the original Gram-Schmidt formula to find the reduced QR 
    factorization of the input matrix. Create the matrices Q and R and set them
    to be equal to 0 matrix. To start calculating matrices Q and R, iterate 
    over every column vector of the input matrix. Storing a copy of the vector, 
    then the vector is set orthagonal to all initialized columns of matrix Q, 
    and storing each element in  matrix R. Normalize this column vector, then 
    repeat for this opreation for all the columns in the input matrix. 
    Returning the matrices Q and R.
    Arguments:
        matrix: A matrix stored as a list of lists.
    Returns:
        The orthonormal matrix, Q of the input matrix and the upper triangular 
        matrix, R fo the input matrix.
    '''
    Q = [[0 for _ in column] for column in matrix]
    R = [[0 for m in matrix] for n in matrix]

    for index, _ in enumerate(matrix):
        vector = matrix[index][:]
        for element in range(0, index):
            orthagonal_operation = orthagonalize(vector, matrix[element])
            vector = orthagonal_operation[0]
            R[index][element] = orthagonal_operation[1]
        normalize_operation = normalize(vector)
        Q[index] = normalize_operation[0]
        R[index][index] = normalize_operation[1]

    return [Q,R]

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

