import numpy as np
import time

def timeit(original_function):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        print("%s took %.2fs to execute" % (original_function.__name__, time.time() - start_time))
        return result

    return wrapper

def multiply_matrix_naive(A,B):
    if A.shape[1] != B.shape[0]:
        raise ValueError

    C = np.zeros((A.shape[0],B.shape[1]))

    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            c = 0
            for k in range(A.shape[1]):
                c += A[i,k]*B[k,j]
            C[i,j] = c

    return C


def multiply_matrix_strassen(A,B):
    def split_matrix(M):
        n = A.shape[0] // 2
        return M[0:n, 0:n], M[0:n,n:], M[n:,0:n], M[n:,n:]

    if A.shape[1] != B.shape[0] or A.shape[0] != A.shape[1] or B.shape[0] != B.shape[1]:
        raise ValueError

    n = A.shape[0] // 2

    if A.shape == (2,2):
        return multiply_matrix_naive(A,B)
    else:
        A11, A12, A21, A22 = split_matrix(A)
        B11, B12, B21, B22 = split_matrix(B)
        M1 = multiply_matrix_strassen(A11 + A22, B11 + B22)
        M2 = multiply_matrix_strassen(A21 + A22, B11)
        M3 = multiply_matrix_strassen(A11, B12 - B22)
        M4 = multiply_matrix_strassen(A22, B21 - B11)
        M5 = multiply_matrix_strassen(A11 + A12, B22)
        M6 = multiply_matrix_strassen(A21 - A11, B11 + B12)
        M7 = multiply_matrix_strassen(A12 - A22, B21 + B22)

        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        C = np.zeros_like(A)
        C[0:n,0:n] = C11
        C[0:n,n:] = C12
        C[n:,0:n] = C21
        C[n:,n:] = C22

        return C

A = np.random.rand(512,512)
B = np.random.rand(512,512)

start_time = time.time()
C1 = multiply_matrix_naive(A,B)
print("%s took %.2fs to execute" % (multiply_matrix_naive.__name__, time.time() - start_time))

start_time = time.time()
C2 = multiply_matrix_strassen(A,B)
print("%s took %.2fs to execute" % (multiply_matrix_strassen.__name__, time.time() - start_time))

assert np.all(C1 - C2 < 1e-9)

#assert np.all(multiply_matrix_naive(A,B) - np.matmul(A,B) < 1e-6)
