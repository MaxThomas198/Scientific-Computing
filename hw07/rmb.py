####################################
# module: rmb.py
# Maxwell Thomas
# A02215231
####################################

import numpy as np

class rmb(object):
    
    @staticmethod
    def rjl(f, a, b, j, l):
        R = [[-1 for c in range(l + 1)] for r in range(j + 1)]
        return np.longdouble(rmb.dynChecker(f, a, b, j, l, R))

    @staticmethod
    def trapezoidArea(f, a, b, n):
        h = (b - a) / n
        sum = 0.0
        for k in range(n):
            term = h * (f(a + k * h) + f(a + (k + 1) * h)) / 2
            sum += term

        return sum

    @staticmethod
    def dynChecker(f, a, b, j, l, R):
        if R[j][l] != -1:
            return R[j][l]
        if l == 1:
            R[j][l] = rmb.trapezoidArea(f, a, b, 2 ** (j - 1))
        elif j < l:
            R[j][l] = 0
        else:
            R[j][l] = rmb.dynChecker(f, a, b, j, l - 1, R) + \
                      (rmb.dynChecker(f, a, b, j, l - 1, R) -
                       rmb.dynChecker(f, a, b, j - 1, l - 1, R)) / (4 ** (l - 1) - 1)
        return R[j][l]
