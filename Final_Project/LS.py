import LA
import QR

def back_substitution(matrix_a: list, Vector: list) -> list:
    '''Calculates the back substitution of a matrix and vector needed to solve 
    a system of equations.
    First we inititialize result as a list of our first solution, which is 
    equal to the second negative index of our input vector multiplied by the 
    division of 1 over the second negative elements of the rows and columns of 
    our input matrix. Next, we create a for loop to go through the elements in 
    the input matrix and subtract 2, then subtract 1, and finally subtract 1 
    again. We then create an inner for loop which gives us the value of our 
    temporary float. We next append that temporary float to our result before 
    finally returning the result.
    
    Arguments:
        matrix_a: A matrix stored as a list of lists.
        Vector: A vector stored as a list.
    
    Returns:
        The corresponding Vector B satisfying Ax=B.
    '''
    result: list = [Vector[-1] * (1/(matrix_a[-1][-1]))]
    for i in range(len(matrix_a)-2, -1, -1):
        temp: float = Vector[i]
        for j in range(len(result)):
            temp -= matrix_a[len(matrix_a)-1-j][i] * result[j]
        temp *= 1/(matrix_a[i][i])
        result.append(temp)
    result = result[::-1]
    return result

def Least_Squares(Vector: list, matrix_a: list) -> list:
    '''Calculates the least squares solution of our input Vector and matrix_a.
    Solves a system of equations following the form A*Ax = A*B (* is the 
    transpose). 1st takes a matrix and return Q and R via Gram-Schmidt 
    decomposistion. The transpose is then taken on Q, which can be denoted by 
    Q_11. Q_11 will then be multiplied by the input vector using mat_vec_mult, 
    and the result can be denoted by Q_12 (Q has now been transformed two 
    times). Finally, we perform back substitution on Q_12 and R to get the 
    solution vector x and returning the result.
    
    Arguments:
        Vector: A vector stored as a list.
        matrix_a: A matrix stored as a list of lists.
    
    Returns:
        The Least Squares solution of the input matrix_a and Vector.
    '''
    Q, R = QR.QR_Householder(matrix_a)
    Q_11 = QR.conjugate_transpose(Q)
    Q_12 = LA.mat_vec_mult(Q_11, Vector)
    back_hand = back_substitution(R, Q_12)
    return back_hand




