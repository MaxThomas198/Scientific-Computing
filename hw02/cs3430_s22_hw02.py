#################################################
# Module: cs3430_s22_hw02.py
# Maxwell Thomas
# A02215231
# bugs to vladimir kulyukin via canvas
#################################################

import numpy as np
import pickle
import os


### =============== Problem 1 =============================

def lu_decomp(a, n):
    """ 
    lu_decomp(a, n) returns u, l such that np.dot(l, u) === a.
    a is an nxn matrix that is reduced to the upper and lower triangular matrices. 
    throws exception when there is no pivot in a column or rows must be swapped
    to create a pivot.
    lu_decomp(a, n) is destructive in that a is destructively modified into u.
    """
    u = a.copy()
    # Identity matrix
    l = np.eye(n, dtype=np.float)
    for i in range(n):
        # Use Gaussian Elimination
        r = u[i + 1:, i] / u[i, i]
        l[i + 1:, i] = r
        u[i + 1:] -= r[:, np.newaxis] * u[i]

    return [u, l]


### =============== Problem 2 =============================

def bsubst(a, n, b, m):
    """
    bsubst uses back substitution to solve ax = b1, b2, ..., bm.
    a is an nxn upper-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm. 
    returns x.
    """
    x = np.zeros_like(b, dtype=np.float)
    x[-1] = b[-1] / a[-1, -1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i:], x[i:])) / a[i, i]

    return x


def fsubst(a, n, b, m):
    """
    fsubst uses forward substitution to solve ax = b1, b2, ..., bm.
    a is an nxn lower-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm.
    returns x.
    """
    x = np.zeros_like(b, dtype=np.float)
    x[0] = b[0] / a[0, 0]
    for i in range(1, n):
        x[i] = (b[i] - np.dot(a[i, :i], x[:i])) / a[i, i]

    return x


def lud_solve(a, n, b, m):
    """
    a is an nxn matrix; b is m nx1 vectors.
    Use forward subst to solve Ly = b for y.
    Use back    subst to solve Ux = y for x.
    Then LUx = Ly = b.
    Returns x.
    """
    [u, l] = lu_decomp(a, n)
    # Forward Substitution
    y = fsubst(l, n, b, m)
    # Back Substitution that returns x
    return bsubst(u, n, y, m)


def lud_solve2(u, l, n, b, m):
    """
    Uses L to transform b to c.
    Then backsubst to solve Ux = c for x.
    Returns x.
    """
    
    return bsubst(u, n, b, m)
