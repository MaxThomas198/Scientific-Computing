#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s22_hw01_uts.py
# description: unit tests for CS 3430: S22: Assignment 01
# bugs to vladimir kulyukin in canvas
##############################################################

import unittest
import numpy as np
import numpy.linalg
from cs3430_s22_hw01 import gje, leibnitz_det, gauss_det, cramer

class cs3430_s22_hw01_uts(unittest.TestCase):

    @staticmethod
    def comp_2d_mats(a, b, err=0.0001):
        """
        Compare two matrices a and b. Returns true if
        a and b are of the same shape and, for every
        legitimate position (i, j), abs(a[i][j] - b[i][j]) <= err.
        """
        ra, ca = a.shape
        rb, cb = b.shape
        if ra != rb:
            return False
        if ca != cb:
            return False
        for r in range(ra):
            for c in range(ca):
                if abs(a[r][c] - b[r][c]) > err:
                    return False
        return True

    ### ================ Problem 1: Unit Tests =====================
    
    def test_hw01_prob01_ut01(self):
        print('\n***** CS3430: S22: HW01: Problem 01: Unit Test 01 ************')
        A = np.array([[0, 1, -3],
                      [2, 3, -1],
                      [4, 5, -2]],
                     dtype=float)
        b = np.array([[-5],
                      [7],
                      [10]], dtype=float)
        x  = gje(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 01: Unit Test 01: pass')

    def test_hw01_prob01_ut02(self):
        print('\n***** CS3430: S22: HW01: Problem 01: Unit Test 02 ************')
        A = np.array(
            [[2, -1, 3],
             [3,  0, 2],
             [-2, 1, 4]],
            dtype=float)
        b = np.array([[4],
                      [5],
                      [6]],
                     dtype=float)
        x  = gje(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 01: Unit Test 02: pass')


    def test_hw01_prob01_ut03(self):
        print('\n***** CS3430: S22: HW01: Problem 01: Unit Test 03 ************')
        A = np.array([[1, 1],
                      [4, 4]],
                     dtype=float)
        b = np.array([[3],
                      [10]],
                     dtype=float)
        x  = gje(A, b)
        assert x is None
        print('CS 3430: S22: HW01: Problem 01: Unit Test 03: pass')

    def test_hw01_prob01_ut04(self):
        print('\n***** CS3430: S22: HW01: Problem 01: Unit Test 04 ************')
        A = np.array([[2, 2],
                      [-2, -2]],
                     dtype=float)
        b = np.array([[5],
                      [3]],
                     dtype=float)
        x  = gje(A, b)
        assert x is None
        print('CS 3430: S22: HW01: Problem 01: Unit Test 04: pass')

    def test_hw01_prob01_ut05(self):
        print('\n***** CS3430: S22: HW01: Problem 01: Unit Test 05 ************')
        A = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[3],
                      [1],
                      [10],
                      [1]],
                     dtype=float)
        x  = gje(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 01: Unit Test 05: pass')


    def test_hw01_prob01_ut06(self):
        print('\n***** CS3430: S22: HW01: Problem 01: Unit Test 06 ************')
        A = np.array([[162., 118., 111., 133.],
                      [ 64.,  37.,  33., 165.],
                      [ 38.,   4., 107.,  86.],
                      [ 98.,  35.,  67., 107.]])
        b = np.array([[10],
                      [15],
                      [200],
                      [140]],
                     dtype=float)
        x  = gje(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 01: Unit Test 06: pass')
        
    def test_hw01_prob01_ut07(self):
        print('\n***** CS3430: S22: HW01: Problem 01: Unit Test 07 ************')
        A = np.array([[446., 163.,  59., 129., 393., 483., 271.,  27., 384.,  58.],
                      [258., 116., 272., 401., 332., 216., 158., 211., 361., 236.],
                      [ 68., 498., 471.,  81., 178., 167., 166., 399., 484., 422.],
                      [338.,  38., 274., 476.,  99., 370., 322., 459., 151., 163.],
                      [380., 106., 421., 314., 425., 332.,  10., 135., 448., 407.],
                      [456., 270., 317., 268.,   3., 394., 250., 354., 135., 310.],
                      [330., 452., 456., 137., 457.,  37., 421.,   5., 357., 165.],
                      [294., 457., 147.,   1., 278., 474., 368., 138., 222., 122.],
                      [231.,   1., 184., 318., 315., 433., 434.,  76.,  71.,  34.],
                      [129., 307., 479., 350., 103., 485., 243., 160., 245., 407.]],
                     dtype=float)
        b = np.array([[1],
                      [2],
                      [3],
                      [4],
                      [5],
                      [6],
                      [7],
                      [8],
                      [9],
                      [10]],
                     dtype=float)
        x  = gje(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)        
        print('CS 3430: S22: HW01: Problem 01: Unit Test 07: pass')

    ## ================ Problem 2: Unit Tests =====================

    def test_hw01_prob02_ut01(self):
        print('\n***** CS3430: S22: HW01: Problem 02: Unit Test 01 ************')
        A = np.array([[0, 1, -3],
                      [2, 3, -1],
                      [4, 5, -2]],
                     dtype=float)
        err = 0.0001
        assert abs(leibnitz_det(A) - np.linalg.det(A)) <= err
        assert abs(gauss_det(A)- np.linalg.det(A)) <= err
        print('CS 3430: S22: HW01: Problem 02: Unit Test 01: pass')

    def test_hw01_prob02_ut02(self):
        print('\n***** CS3430: S22: HW01: Problem 02: Unit Test 02 ************')
        A = np.array(
            [[2, -1, 3],
             [3,  0, 2],
             [-2, 1, 4]],
            dtype=float)
        err = 0.0001
        assert abs(leibnitz_det(A) - np.linalg.det(A)) <= err
        assert abs(gauss_det(A)- np.linalg.det(A)) <= err
        print('CS 3430: S22: HW01: Problem 02: Unit Test 02: pass')

    def test_hw01_prob02_ut03(self):
        print('\n***** CS3430: S22: HW01: Problem 02: Unit Test 03 ************')
        A = np.array([[1, 1],
                      [4, 4]],
                     dtype=float)
        err = 0.0001
        assert abs(leibnitz_det(A) - np.linalg.det(A)) <= err
        assert abs(gauss_det(A)- np.linalg.det(A)) <= err
        print('CS 3430: S22: HW01: Problem 02: Unit Test 03: pass')

    def test_hw01_prob02_ut04(self):
        print('\n***** CS3430: S22: HW01: Problem 02: Unit Test 04 ************')
        A = np.array([[2, 2],
                      [-2, -2]],
                     dtype=float)
        err = 0.0001
        assert abs(leibnitz_det(A) - np.linalg.det(A)) <= err
        assert abs(gauss_det(A)- np.linalg.det(A)) <= err
        print('CS 3430: S22: HW01: Problem 02: Unit Test 04: pass')

    def test_hw01_prob02_ut05(self):
        print('\n***** CS3430: S22: HW01: Problem 02: Unit Test 05 ************')
        A = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        err = 0.0001
        assert abs(leibnitz_det(A) - np.linalg.det(A)) <= err
        assert abs(gauss_det(A)- np.linalg.det(A)) <= err
        print('CS 3430: S22: HW01: Problem 02: Unit Test 05: pass')

    def test_hw01_prob02_ut06(self):
        print('\n***** CS3430: S22: HW01: Problem 02: Unit Test 06 ************')
        A = np.array([[162., 118., 111., 133.],
                      [ 64.,  37.,  33., 165.],
                      [ 38.,   4., 107.,  86.],
                      [ 98.,  35.,  67., 107.]])
        err = 0.0001
        assert abs(leibnitz_det(A) - np.linalg.det(A)) <= err
        assert abs(gauss_det(A)- np.linalg.det(A)) <= err
        print('CS 3430: S22: HW01: Problem 02: Unit Test 06: pass')

    def test_hw01_prob02_ut07(self):
        print('\n***** CS3430: S22: HW01: Problem 02: Unit Test 07 ************')
        A = np.array([[446., 163.,  59., 129., 393., 483., 271.,  27., 384.,  58.],
                      [258., 116., 272., 401., 332., 216., 158., 211., 361., 236.],
                      [ 68., 498., 471.,  81., 178., 167., 166., 399., 484., 422.],
                      [338.,  38., 274., 476.,  99., 370., 322., 459., 151., 163.],
                      [380., 106., 421., 314., 425., 332.,  10., 135., 448., 407.],
                      [456., 270., 317., 268.,   3., 394., 250., 354., 135., 310.],
                      [330., 452., 456., 137., 457.,  37., 421.,   5., 357., 165.],
                      [294., 457., 147.,   1., 278., 474., 368., 138., 222., 122.],
                      [231.,   1., 184., 318., 315., 433., 434.,  76.,  71.,  34.],
                      [129., 307., 479., 350., 103., 485., 243., 160., 245., 407.]],
                     dtype=float)
        err = 0.0001
        gd = gauss_det(A)
        nd = np.linalg.det(A)
        assert abs(float(str(gd)[:10]) - float(str(nd)[:10])) <= err
        print('CS 3430: S22: HW01: Problem 02: Unit Test 07: pass')

    # ### ================ Problem 3: Unit Tests =====================

    def test_hw01_prob03_ut01(self):
        print('\n***** CS3430: S22: HW01: Problem 03: Unit Test 01 ************')
        A = np.array([[0, 1, -3],
                      [2, 3, -1],
                      [4, 5, -2]],
                     dtype=float)
        b = np.array([[-5],
                      [7],
                      [10]], dtype=float)
        x  = cramer(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 03: Unit Test 01: pass')

    def test_hw01_prob03_ut02(self):
        print('\n***** CS3430: S22: HW01: Problem 03: Unit Test 02 ************')
        A = np.array(
            [[2, -1, 3],
             [3,  0, 2],
             [-2, 1, 4]],
            dtype=float)
        b = np.array([[4],
                      [5],
                      [6]],
                     dtype=float)
        x  = cramer(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 03: Unit Test 02: pass')

    def test_hw01_prob03_ut03(self):
        print('\n***** CS3430: S22: HW01: Problem 03: Unit Test 03 ************')
        A = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[3],
                      [1],
                      [10],
                      [1]],
                     dtype=float)
        x  = cramer(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 03: Unit Test 03: pass')

    def test_hw01_prob03_ut04(self):
        print('\n***** CS3430: S22: HW01: Problem 03: Unit Test 04 ************')
        A = np.array([[162., 118., 111., 133.],
                      [ 64.,  37.,  33., 165.],
                      [ 38.,   4., 107.,  86.],
                      [ 98.,  35.,  67., 107.]])
        b = np.array([[10],
                      [15],
                      [200],
                      [140]],
                     dtype=float)
        x = cramer(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 03: Unit Test 04: pass')

    def test_hw01_prob03_ut05(self):
        print('\n***** CS3430: S22: HW01: Problem 03: Unit Test 05 ************')
        A = np.array([[446., 163.,  59., 129., 393., 483., 271.,  27., 384.,  58.],
                      [258., 116., 272., 401., 332., 216., 158., 211., 361., 236.],
                      [ 68., 498., 471.,  81., 178., 167., 166., 399., 484., 422.],
                      [338.,  38., 274., 476.,  99., 370., 322., 459., 151., 163.],
                      [380., 106., 421., 314., 425., 332.,  10., 135., 448., 407.],
                      [456., 270., 317., 268.,   3., 394., 250., 354., 135., 310.],
                      [330., 452., 456., 137., 457.,  37., 421.,   5., 357., 165.],
                      [294., 457., 147.,   1., 278., 474., 368., 138., 222., 122.],
                      [231.,   1., 184., 318., 315., 433., 434.,  76.,  71.,  34.],
                      [129., 307., 479., 350., 103., 485., 243., 160., 245., 407.]],
                     dtype=float)
        b = np.array([[1],
                      [2],
                      [3],
                      [4],
                      [5],
                      [6],
                      [7],
                      [8],
                      [9],
                      [10]],
                     dtype=float)
        x  = cramer(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 03: Unit Test 05: pass')

    def test_hw01_prob03_ut06(self):
        print('\n***** CS3430: S22: HW01: Problem 03: Unit Test 06 ************')
        A = np.array([[446., 163.,  59., 129., 393., 483., 271.,  27., 384.,  58.],
                      [258., 116., 272., 401., 332., 216., 158., 211., 361., 236.],
                      [ 68., 498., 471.,  81., 178., 167., 166., 399., 484., 422.],
                      [338.,  38., 274., 476.,  99., 370., 322., 459., 151., 163.],
                      [380., 106., 421., 314., 425., 332.,  10., 135., 448., 407.],
                      [456., 270., 317., 268.,   3., 394., 250., 354., 135., 310.],
                      [330., 452., 456., 137., 457.,  37., 421.,   5., 357., 165.],
                      [294., 457., 147.,   1., 278., 474., 368., 138., 222., 122.],
                      [231.,   1., 184., 318., 315., 433., 434.,  76.,  71.,  34.],
                      [129., 307., 479., 350., 103., 485., 243., 160., 245., 407.]],
                     dtype=float)
        b = np.array([[2],
                      [3],
                      [4],
                      [5],
                      [6],
                      [7],
                      [8],
                      [9],
                      [10],
                      [11]],
                     dtype=float)
        x  = cramer(A, b)
        bb = np.dot(A, x)
        assert cs3430_s22_hw01_uts.comp_2d_mats(b, bb)
        print('CS 3430: S22: HW01: Problem 03: Unit Test 06: pass')
        
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
