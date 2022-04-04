######################################################
# module: cs3430_s22_hw01.py
# Maxwell Thomas
# A02215231
######################################################

import numpy as np
import random


## If you need to define auxiliary functions, you may define them
## in this file.

### ============= Problem 1 (Gauss-Jordan Elimination) ===============


def gje(a, b):
    """ Gauss-Jordan Elimination to solve Ax = b. """
    # n is matrix size
    n = len(b)
    x = np.matrix.copy(b)
    # Elimination phase
    for c in range(a.shape[1]):
        if find_value(a, c) != c:
            #  Switch rows
            a[[find_value(a, c), c], :] = a[[c, find_value(a, c)], :]

        for r in range(c + 1, a.shape[0]):
            factor = a[r, c] / a[c, c]
            a[r, :] = a[r, :] - factor * a[c, :]

# Back substitution
    for r in range(n - 1, -1, -1):
        x[r] = (x[r] - np.dot(a[r, r + 1:n], x[r + 1:n])) / a[r, r]

    return x


## ============== Problem 2 (Determinants) ========================

def random_mat(nr, nc, lower, upper):
    """ Generate an nrxnc matrix of random numbers in [lower, upper]. """
    m = np.zeros((nr, nc))
    for r in range(nr):
        for c in range(nc):
            m[r][c] = random.randint(lower, upper)
    return m

def leibnitz_det(a):
    """ Compute determinant of nxn matrix a with Leibnitz's Formula. """
    def minor_matrices(a, i, j):
        c = a[:]
        c = np.delete(c, (i), axis=0)
        return [np.delete(r, (j), axis=0) for r in (c)]

    # n is matrix size
    n = len(a)
    # special cases
    if n == 1: return a[0][0]
    if n == 2: return a[0][0] * a[1][1] - a[0][1] * a[1][0]

    sum = 0
    for i in range(0, n):
        m = minor_matrices(a, 0, i)
        #recursive calling
        sum = sum + ((-1) ** i) * a[0][i] * leibnitz_det(m)
    return sum


def gauss_det(a):
    """ Compute determinant of nxn matrix a with Gaussian elimination. """
    a = np.matrix.copy(a)
    row_interchanges = 0
    #  Use Gauss Elimination to get echelon form

    for c in range(a.shape[1]):
        if find_value(a, c) != c:
            #  Switch rows
            a[[find_value(a, c), c], :] = a[[c, find_value(a, c)], :]
            row_interchanges += 1

        for r in range(c + 1, a.shape[0]):
            factor = a[r, c] / a[c, c]
            a[r, :] = a[r, :] - factor * a[c, :]

    return a.diagonal().prod() * (-1) ** row_interchanges


# Find first non-zero value starting from diagonal element
def find_value(a, n):
    r = n
    while r < a.shape[0] and a[r, n] == 0:
        r += 1
    return r

## ============== Problem 3 (Cramer's Rule) ======================
def cramer(a, b):
    """ Solve Ax = b with Cramer's Rule. """
    n = b.size
    detA = leibnitz_det(a)
    x = b.copy()
    b = b.reshape(-1)
    for i in range(n):
        test = a.copy()
        test[:, i] = b
        x[i] = (leibnitz_det(test) / detA)
    return x


if __name__ == '__main__':
    pass

