#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s22_hw02_uts.py
# description: unit tests for CS 3430: S22: Assignment 02
# bugs to vladimir kulyukin in canvas
##############################################################

import unittest
import numpy as np
import numpy.linalg
import pickle
from cs3430_s22_hw02 import lu_decomp, bsubst, fsubst, lud_solve, lud_solve2

class cs3430_s22_hw02_uts(unittest.TestCase):

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

    @staticmethod
    def comp_1d_mats(a, b, err=0.0001):
        """
        Compare two array a and b. Returns true if
        a and b are of the same shape and, for every
        legitimate position (i, j), abs(a[i][j] - b[i][j]) <= err.
        """
        assert len(a.shape) == len(b.shape) == 1
        ca = a.shape[0]
        cb = b.shape[0]
        if ca != cb:
            return False
        for i in range(ca):
            if abs(a[i] - b[i]) > err:
                return False
        return True

    def lud_test(self, a, err=0.0001, prnt_flag=True):
        r, c = a.shape
        assert r == c
        u, l = lu_decomp(a.copy(), r)
        m2 = np.matmul(l, u)
        assert cs3430_s22_hw02_uts.comp_2d_mats(a, m2)    
        if prnt_flag:
            print('U:')
            print(u)
            print('L:')
            print(l)
            print('Original Matrix:')
            print(a)
            print('L*U:')
            print(m2)

    def check_lin_sys_sol(self, a, n, b, m, x, err=0.0001):
        ra, ca = a.shape
        assert ra == n
        assert ca == n
        assert b.shape[0] == n
        assert b.shape[1] == m
        assert b.shape == x.shape
        for c in range(m):
            bb = np.array([np.matmul(a, x[:,c])]).T
            for r in range(n):
                assert abs(b[r][c] - bb[r][0]) <= err

    def lud_solve_test(self, a, n, b, m, err=0.0001, prnt_flag=True):
        x = lud_solve(a, n, b, m)
        self.check_lin_sys_sol(a, n, b, m, x, err=err)
        if prnt_flag:
            print('A:')
            print(a)
            print('b:')
            print(b)
            print('x:')
            print(x)
            print('A*x:')
            print(np.dot(a, x))

    def lud_solve2_test(self, a, n, b, m, err=0.0001, prnt_flag=True):
        aa = a.copy()
        u, l = lu_decomp(aa, n)
        bb = b.copy()
        x = lud_solve2(u, l, n, bb, m)
        self.check_lin_sys_sol(a, n, b, m, x, err=err)
        if prnt_flag:
            print('A:')
            print(a)
            print('b:')
            print(b)
            print('x:')
            print(x)
            print('A*x:')
            print(np.dot(a, x))

    def load_lin_systems(self, file_name):
        with open(file_name, 'rb') as fp:
            return pickle.load(fp)

    def lud_solve_test_lin_systems(self, file_name, err=0.0001):
        print('Testing LUD on {} ...'.format(file_name))
        lu_failures = []
        lin_systems = self.load_lin_systems(file_name)
        for A, b in lin_systems:
            try:
                self.lud_solve_test(A, A.shape[0], b, 1, err=err, prnt_flag=False)
            except Exception as e:
                print(e)
                lu_failures.append((A, b))
        print('Testing LUD had {} failures...'.format(len(lu_failures)))
        assert len(lu_failures) == 0
            
    ### ================ Problem 1: Unit Tests =====================

    def test_hw02_prob01_ut01(self):
        print('\n***** CS3430: S22: HW01: Problem 01: Unit Test 01 ************')
        A = np.array([[2, 3, -1],
                      [0, 1, -3],
                      [4, 5, -2]],
                     dtype=float)
        self.lud_test(A, prnt_flag=False)
        print('CS 3430: S22: HW01: Problem 01: Unit Test 01: pass')


    def test_hw02_prob01_ut02(self):
        print('\n***** CS3430: S22: HW02: Problem 01: Unit Test 02 ************')
        A = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        self.lud_test(A, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 01: Unit Test 02: pass')

    def test_hw02_prob01_ut03(self):
        print('\n***** CS3430: S22: HW02: Problem 01: Unit Test 03 ************')
        A = np.array([[162., 118., 111., 133.],
                      [ 64.,  37.,  33., 165.],
                      [ 38.,   4., 107.,  86.],
                      [ 98.,  35.,  67., 107.]])
        self.lud_test(A, prnt_flag=False)        
        print('CS 3430: S22: HW02: Problem 01: Unit Test 03: pass')
        
    def test_hw02_prob01_ut04(self):
        print('\n***** CS3430: S22: HW02: Problem 01: Unit Test 04 ************')
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
        self.lud_test(A, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 01: Unit Test 04: pass')

    def test_hw02_prob01_ut05(self):
        print('\n***** CS3430: S22: HW02: Problem 01: Unit Test 05 ************')
        A = np.array([[1, 3, -1],
                      [2, 8,  4],
                      [-1, 3, 4]],
                     dtype=float)
        self.lud_test(A, prnt_flag=False)        
        print('CS 3430: S22: HW02: Problem 01: Unit Test 05: pass')
        
    ### ================ Problem 2: Unit Tests =====================

    def test_hw02_prob02_ut01(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 01 ************')
        a = np.array([[1, 3, -1],
                      [0, 2, 6],
                      [0, 0, -15]],
                     dtype=float)
        b = np.array([[-4, 5],
                      [10, 11],
                      [-30, 28]],
                     dtype=float)

        x = bsubst(a, 3, b, 2)
        b0 = np.dot(a, x[:,0])
        assert cs3430_s22_hw02_uts.comp_1d_mats(b[:,0], b0)
        b1 = np.dot(a, x[:,1])
        assert cs3430_s22_hw02_uts.comp_1d_mats(b[:,1], b1)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 01: pass')

    def test_hw02_prob02_ut02(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 02 ************')
        a = np.array([[1, 3, -1],
                      [0, 2,  6],
                      [0, 0, -15]],
                 dtype=float)
        b = np.array([[-4],
                      [10],
                      [-30]],
                     dtype=float)
        x = bsubst(a, 3, b, 1)
        b0 = np.dot(a, x[:,0])
        assert cs3430_s22_hw02_uts.comp_1d_mats(b[:,0], b0)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 02: pass')

    def test_hw02_prob02_ut03(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 03 ************')
        a = np.array([[1, 0, 0],
                      [2, 1, 0],
                      [-1, 3, 1]],
                     dtype=float)
        b = np.array([[-4],
                      [2],
                      [4]],
                     dtype=float)
        x = fsubst(a, 3, b, 1)
        b0 = np.dot(a, x[:,0])
        assert cs3430_s22_hw02_uts.comp_1d_mats(b[:,0], b0)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 03: pass')

    def test_hw02_prob02_ut04(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 04 ************')
        a = np.array([[2, 0, 0],
                      [2, 3, 0],
                      [-1, 3, 4]],
                     dtype=float)
        b = np.array([[-4],
                      [2],
                      [4]],
                     dtype=float)
        x = fsubst(a, 3, b, 1)
        b0 = np.dot(a, x[:,0])
        assert cs3430_s22_hw02_uts.comp_1d_mats(b[:,0], b0)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 04: pass')

    def test_hw02_prob02_ut05(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 05 ************')
        a = np.array([[1, 0, 0],
                      [2, 1, 0],
                      [-1, 3, 1]],
                     dtype=float)
        b = np.array([[-4, 10],
                      [ 2, 12],
                      [ 4, 21]],
                     dtype=float)
        x = fsubst(a, 3, b, 2)
        b0 = np.dot(a, x[:,0])
        assert cs3430_s22_hw02_uts.comp_1d_mats(b[:,0], b0)
        b1 = np.dot(a, x[:,1])
        assert cs3430_s22_hw02_uts.comp_1d_mats(b[:,1], b1)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 05: pass')

    def test_hw02_prob02_ut06(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 06 ************')
        a = np.array([[12, 0, 0],
                      [2, 21, 0],
                      [-1, 3, 16]],
                     dtype=float)
        b = np.array([[-4, 10],
                      [ 2, 12],
                      [ 4, 21]],
                     dtype=float)
        x = fsubst(a, 3, b, 2)
        b0 = np.dot(a, x[:,0])
        assert cs3430_s22_hw02_uts.comp_1d_mats(b[:,0], b0)
        b1 = np.dot(a, x[:,1])
        assert cs3430_s22_hw02_uts.comp_1d_mats(b[:,1], b1)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 06: pass')

    def test_hw02_prob02_ut07(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 07 ************')
        a = np.array([[1, 3, -1],
                      [2, 8, 4],
                      [-1, 3, 4]],
                     dtype=float)
        b = np.array([[-4],
                      [2],
                      [4]],
                     dtype=float)
        err = 0.0001
        self.lud_solve_test(a, 3, b, 1, err=err, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 07: pass')

    def test_hw02_prob02_ut08(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 08 ************')
        a = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[4.0],
                      [-1.0],
                      [3.0],
                      [5.0]])
        err = 0.0001
        self.lud_solve_test(a, 4, b, 1, err=err, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 08: pass')

    def test_hw02_prob02_ut09(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 09 ************')
        a = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[4.0,  1.0],
                      [-1.0, 2.0],
                      [3.0,  3.0],
                      [5.0,  4.0]])
        err = 0.0001
        self.lud_solve_test(a, 4, b, 2, err=err, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 09: pass')

    def test_hw02_prob02_ut10(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 10 ************')
        a = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[4.0,  1.0, 10.0],
                      [-1.0, 2.0, 15.0],
                      [3.0,  3.0, 42.0],
                      [5.0,  4.0, 53.0]])
        err = 0.0001
        self.lud_solve_test(a, 4, b, 3, err=err, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 10: pass')

    def test_hw02_prob02_ut11(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 11 ************')
        a = np.array([[1, 3, -1],
                      [2, 8, 4],
                      [-1, 3, 4]],
                     dtype=float)
        b = np.array([[-4],
                      [2],
                      [4]],
                     dtype=float)
        err = 0.0001
        self.lud_solve2_test(a, 3, b, 1, err=err, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 11: pass')

    def test_hw02_prob02_ut12(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 12 ************')
        a = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[4.0],
                      [-1.0],
                      [3.0],
                      [5.0]])
        err = 0.0001
        self.lud_solve2_test(a, 4, b, 1, err=err, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 12: pass')

    def test_hw02_prob02_ut13(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 13 ************')
        a = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[4.0,  1.0, 10.0],
                      [-1.0, 2.0, 15.0],
                      [3.0,  3.0, 42.0],
                      [5.0,  4.0, 53.0]])
        err = 0.0001
        self.lud_solve2_test(a, 4, b, 3, err=err, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 13: pass')

    def test_hw02_prob02_ut14(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 14 ************')
        a = np.array([[446., 163.,  59., 129., 393., 483., 271.,  27., 384.,  58.],
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
        b = np.array(
            [[336.],
             [488.],
             [ 46.],
             [351.],
             [395.],
             [466.],
             [360.],
             [288.],
             [498.],
             [137.]],
            dtype=float)
        err = 0.0001
        self.lud_solve2_test(a, 10, b, 1, err=err, prnt_flag=False)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 14: pass')

    def test_hw02_prob02_ut15(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 15 ************')
        self.lud_solve_test_lin_systems('ab_5x5.pck', err=0.0001)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 15: pass')

    def test_hw02_prob02_ut16(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 16 ************')
        self.lud_solve_test_lin_systems('ab_50x50.pck', err=0.0001)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 16: pass')

    def test_hw02_prob02_ut17(self):
        print('\n***** CS3430: S22: HW02: Problem 02: Unit Test 17 ************')
        self.lud_solve_test_lin_systems('ab_100x100.pck', err=0.0001)
        print('CS 3430: S22: HW02: Problem 02: Unit Test 17: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
    pass
