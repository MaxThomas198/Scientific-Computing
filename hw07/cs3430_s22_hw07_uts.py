#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s22_hw07_uts.py
# description: unit tests for CS 3430: S22: Assignment 07
##############################################################

import unittest
import math
import numpy as np
from poly_parser import poly_parser
from tof import tof
from drv import drv
from cdd import cdd
from rxp import rxp
from rmb import rmb

class cs3430_s22_hw07_uts(unittest.TestCase):

    ### ================ Problem 1: Unit Tests =====================


    def test_hw07_prob01_ut01(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 01 ************')
        f = lambda x: math.cos(x)
        ## 1. compute approximate value av
        av = cdd.drv1_ord2(f, 0.8, 0.01)
        ## 2. compute true value tv
        tv = -math.sin(0.8)
        ## 3. set error level
        err = 0.0001
        ## 4. make sure you return np.longdouble for max precision
        assert isinstance(av, np.longdouble)
        ## 5. compare av and tv at specified error level
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 01: pass')

    def test_hw07_prob01_ut02(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 02 ************')
        f = lambda x: math.cos(x)
        av = cdd.drv1_ord4(f, 0.8, 0.01)
        tv = -math.sin(0.8)
        err = 0.000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 02: pass')

    def test_hw07_prob01_ut03(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 03 ************')
        f = lambda x: math.cos(x)
        av = cdd.drv1_ord4(f, 0.8, 0.001)
        tv = -math.sin(0.8)
        err = 0.000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 03: pass')

    def test_hw07_prob01_ut04(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 04 ************')
        f = lambda x: math.sin(x)
        av = cdd.drv1_ord2(f, 0.8, 0.01)
        tv = math.cos(0.8)
        err = 0.0001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 04: pass')

    def test_hw07_prob01_ut05(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 05 ************')
        f = lambda x: math.sin(x)
        av = cdd.drv1_ord4(f, 0.8, 0.01)
        tv = math.cos(0.8)
        err = 0.000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 05: pass')

    def test_hw07_prob01_ut06(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 06 ************')
        f = lambda x: math.sin(x)
        av = cdd.drv1_ord4(f, 0.8, 0.000001)
        tv = math.cos(0.8)
        err = 0.00000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 06: pass')

    def test_hw07_prob01_ut07(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 07 ************')
        f = lambda x: math.e**x
        av = cdd.drv1_ord2(f, 0.8, 0.000001)
        tv = f(0.8)
        err = 0.00000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 07: pass')

    def test_hw07_prob01_ut08(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 08 ************')
        f = lambda x: math.e**(2.0*x)
        ## df is the ground truth derivative function
        df = lambda x: 2.0*(math.e**(2.0*x))
        x = 3.0
        h = 0.001
        av = cdd.drv1_ord4(f, x, h)
        tv = df(x)
        err = 0.00000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 08: pass')

    def test_hw07_prob01_ut09(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 09 ************')
        f = lambda x: math.e**(-2.0*x)
        ## df is the ground truth derivative function
        df = lambda x: -2.0*(math.e**(-2.0*x))
        x = 3.0
        h = 0.001
        av = cdd.drv1_ord4(f, x, h)
        tv = df(x)
        err = 0.00000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 09: pass')

    def test_hw07_prob01_ut10(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 10 ************')
        ## f(x) = ln(x)
        f = lambda x: math.log(x, math.e)
        ## df is the ground truth derivative function
        df = lambda x: 1.0/x
        x = 0.25
        h = 0.0001
        av = cdd.drv1_ord4(f, x, h)
        tv = df(x)
        err = 0.00000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 10: pass')

    def test_hw07_prob01_ut11(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 11 ************')
        f = lambda x: 2*(x**3.0) + 3.0*x
        ## rename poly_parser if necessary.
        df = tof.tof(drv.drv(poly_parser.parse_sum('2x^3 + 3x^1')))
        print(drv.drv(poly_parser.parse_sum('2x^3 + 3x^1')))
        print(df)
        x = 1.0
        h = 0.0001
        av = cdd.drv1_ord2(f, x, h)
        tv = df(x)
        err = 0.00001
        assert abs(tv - 9.0) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 11: pass')

    def test_hw07_prob01_ut12(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 12 ************')
        f = lambda x: 2*(x**3.0) + 3.0*x
        ## rename poly_parser if necessary.
        df = tof.tof(drv.drv(poly_parser.parse_sum('2x^3 + 3x^1')))
        x = 1.0
        h = 0.0001
        av = cdd.drv1_ord4(f, x, h)
        tv = df(x)
        err = 0.00000001
        assert abs(tv - 9.0) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 12: pass')

    def test_hw07_prob01_ut13(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 13 ************')
        f = lambda x: 4*(x**3.0) - 3.0*(x**2.0) + 5.0*x - 10.0
        ## rename poly_parser if necessary.
        df = tof.tof(drv.drv(poly_parser.parse_sum('4x^3 - 3x^2 + 5x^1 - 10x^0')))
        x = 1.0
        h = 0.0001
        av = cdd.drv1_ord2(f, x, h)
        tv = df(x)
        err = 0.0000001
        assert abs(tv - 11.0) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 13: pass')

    def test_hw07_prob01_ut14(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 14 ************')
        f = lambda x: 4*(x**3.0) - 3.0*(x**2.0) + 5.0*x - 10.0
        ## rename poly_parser if necessary.
        df = tof.tof(drv.drv(poly_parser.parse_sum('4x^3 - 3x^2 + 5x^1 - 10x^0')))
        x = 1.0
        h = 0.0001
        av = cdd.drv1_ord4(f, x, h)
        tv = df(x)
        err = 0.0000001
        assert abs(tv - 11.0) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 14: pass')

    def test_hw07_prob01_ut15(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 15 ************')
        f = lambda x: 4*(x**5.0) - 3.0*(x**-3.0) + 10.0*(x**2) - 5.0*x
        ## rename poly_parser if necessary.
        df = tof.tof(drv.drv(poly_parser.parse_sum('4x^5 - 3x^-3 + 10x^2 - 5x^1')))
        x = 0.5
        h = 0.0001
        av = cdd.drv1_ord4(f, x, h)
        tv = df(x)
        err = 0.0000001
        assert abs(tv - 150.25) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 15: pass')

    def test_hw07_prob01_ut16(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 16 ************')
        f = lambda x: math.cos(x)
        ## df is the ground truth derivative function
        df = lambda x: -math.cos(x)
        x = 0.8
        h = 0.01
        av = cdd.drv2_ord2(f, x, h)
        tv = df(x)
        err = 0.0001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 16: pass')

    def test_hw07_prob01_ut17(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 17 ************')
        f = lambda x: math.cos(x)
        ## df is the ground truth second derivative function
        df = lambda x: -math.cos(x)
        x = 0.8
        h = 0.001
        av = cdd.drv2_ord2(f, x, h)
        tv = df(x)
        err = 0.00001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 17: pass')

    def test_hw07_prob01_ut18(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 18 ************')
        f = lambda x: math.cos(x)
        ## df is the ground truth second derivative function
        df = lambda x: -math.cos(x)
        x = 0.8
        h = 0.001
        av = cdd.drv2_ord4(f, x, h)
        tv = df(x)
        err = 0.00000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 18: pass')

    def test_hw07_prob01_ut19(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 19 ************')
        f = lambda x: math.log(x, math.e)
        ## df is the ground truth second derivative function
        df = lambda x: -(x**(-2.0))
        x = 1.0
        h = 0.001
        av = cdd.drv2_ord2(f, x, h)
        tv = df(x)
        err = 0.00001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 19: pass')

    def test_hw07_prob01_ut20(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 20 ************')
        f = lambda x: math.log(x, math.e)
        ## df is the ground truth second derivative function
        df = lambda x: -(x**(-2.0))
        x = 1.0
        h = 0.001
        av = cdd.drv2_ord4(f, x, h)
        tv = df(x)
        err = 0.00000001
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 20: pass')

    def test_hw07_prob01_ut21(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 21 ************')
        f = lambda x: 2.0*(x**3.0) + 3.0*x
        ## df is the ground truth second derivative function
        df = lambda x: 12.0*x
        x = 2.0
        h = 0.001
        av = cdd.drv2_ord2(f, x, h)
        tv = df(x)
        err = 0.0001
        assert abs(tv - 24.0) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 21: pass')

    def test_hw07_prob01_ut22(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 22 ************')
        f = lambda x: 2.0*(x**3.0) + 3.0*x
        ## df is the ground truth second derivative function
        df = lambda x: 12.0*x
        x = 2.0
        h = 0.001
        av = cdd.drv2_ord4(f, x, h)
        tv = df(x)
        err = 0.0000001
        assert abs(tv - 24.0) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 22: pass')

    def test_hw07_prob01_ut23(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 23 ************')
        f = lambda x: 4*(x**5.0) - 3.0*(x**-3.0) + 10.0*(x**2.0) - 5.0*x
        df = lambda x: 80.0*(x**3.0) - 36.0*(x**-5.0) + 20.0
        x = 1.0
        h = 0.0001
        av = cdd.drv2_ord2(f, x, h)
        tv = df(x)
        err = 0.0001
        assert abs(tv - 64.0) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 23: pass')

    def test_hw07_prob01_ut24(self):
        print('\n***** CS3430: S22: HW07: Problem 01: Unit Test 24 ************')
        f = lambda x: 4*(x**5.0) - 3.0*(x**-3.0) + 10.0*(x**2.0) - 5.0*x
        df = lambda x: 80.0*(x**3.0) - 36.0*(x**-5.0) + 20.0
        x = 1.0
        h = 0.0001
        av = cdd.drv2_ord4(f, x, h)
        tv = df(x)
        err = 0.000001
        assert abs(tv - 64.0) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 01: Unit Test 24: pass')

    ### ================ Problem 2: Unit Tests =====================

    def test_hw07_prob02_ut01(self):
        print('\n***** CS3430: S22: HW07: Problem 02: Unit Test 01 ************')
        def f(x):
            n = math.sin(math.sqrt(x**2 + x)/(math.cos(x) - x))**2.0
            d = math.sin((math.sqrt(x) - 1.0)/math.sqrt(x**2.0 + 1))
            return n/d
        err = 0.000001
        x = 0.25
        h = 0.01
        av = rxp.drv1(f, cdd.drv1_ord2, 0.25, 0.01)
        tv = -9.069752978901475
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 02: Unit Test 01: pass')

    def test_hw07_prob02_ut02(self):
        print('\n***** CS3430: S22: HW07: Problem 02: Unit Test 02 ************')
        def f(x):
            n = math.sin(math.sqrt(x**2 + x)/(math.cos(x) - x))**2.0
            d = math.sin((math.sqrt(x) - 1.0)/math.sqrt(x**2.0 + 1))
            return n/d
        err = 0.000001
        x = 0.25
        h = 0.01
        av = rxp.drv1(f, cdd.drv1_ord4, 0.25, 0.01)
        tv = -9.066741009453901
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 02: Unit Test 02: pass')

    def test_hw07_prob02_ut03(self):
        print('\n***** CS3430: S22: HW07: Problem 02: Unit Test 03 ************')
        def f(x):
            n = math.sin(math.sqrt(x**2 + x)/(math.cos(x) - x))**2.0
            d = math.sin((math.sqrt(x) - 1.0)/math.sqrt(x**2.0 + 1))
            return n/d
        err = 0.000001
        x = 0.25
        h = 0.01
        av = rxp.drv2(f, cdd.drv1_ord2, 0.25, 0.01)
        tv = -9.066701400261493
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 02: Unit Test 03: pass')

    def test_hw07_prob02_ut04(self):
        print('\n***** CS3430: S22: HW07: Problem 02: Unit Test 04 ************')
        def f(x):
            n = math.sin(math.sqrt(x**2 + x)/(math.cos(x) - x))**2.0
            d = math.sin((math.sqrt(x) - 1.0)/math.sqrt(x**2.0 + 1))
            return n/d
        err = 0.000001
        x = 0.25
        h = 0.01
        av = rxp.drv2(f, cdd.drv1_ord4, 0.25, 0.01)
        tv = -9.066688197197351
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 02: Unit Test 04: pass')

    def test_hw07_prob02_ut05(self):
        print('\n***** CS3430: S22: HW07: Problem 02: Unit Test 05 ************')
        f = lambda x: 4*(x**5.0) - 3.0*(x**-3.0) + 10.0*(x**2) - 5.0*x
        ## rename poly_parser if necessary.
        df = tof.tof(drv.drv(poly_parser.parse_sum('4x^5 - 3x^-3 + 10x^2 - 5x^1')))
        x = 0.5
        h = 0.0001
        av = rxp.drv1(f, cdd.drv1_ord4, x, h)
        tv = df(x)
        err = 0.0000001
        assert abs(tv - 150.25) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 02: Unit Test 05: pass')

    def test_hw07_prob02_ut06(self):
        print('\n***** CS3430: S22: HW07: Problem 02: Unit Test 06 ************')
        f = lambda x: 4*(x**5.0) - 3.0*(x**-3.0) + 10.0*(x**2) - 5.0*x
        ## rename poly_parser if necessary.
        df = tof.tof(drv.drv(poly_parser.parse_sum('4x^5 - 3x^-3 + 10x^2 - 5x^1')))
        x = 0.5
        h = 0.0001
        av = rxp.drv2(f, cdd.drv1_ord2, x, h)
        tv = df(x)
        err = 0.0000001
        assert abs(tv - 150.25) <= err
        assert isinstance(av, np.longdouble)
        assert abs(av - tv) <= err
        print('av={}'.format(av))
        print('tv={}'.format(tv))
        print('CS 3430: S22: HW07: Problem 02: Unit Test 06: pass')

    ### ================ Problem 3: Unit Tests =====================

    def test_hw07_prob03_ut01(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 01 ************')
        def f(x):
            return math.e**(-(x**2.0))
        err = 0.00001
        tv  = 0.683939720585721167
        ## Approximating integral of f(x) on [a=0, b=1] with R[1,1].
        av  = rmb.rjl(f, 0, 1, 1, 1)
        assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 01: pass')

    def test_hw07_prob03_ut02(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 02 ************')
        def f(x):
            return math.e**(-(x**2.0))
        err = 0.00001
        tv  = 0.73137025182856307826
        ## Approximating integral of f(x) on [a=0, b=1] with R[2,1].
        av  = rmb.rjl(f, 0, 1, 2, 1)
        assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 02: pass')

    def test_hw07_prob03_ut03(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 03 ************')
        def f(x):
            return math.e**(-(x**2.0))
        err = 0.00001
        tv = 0.74298409780038121575
        ## Approximating integral of f(x) on [a=0, b=1] with R[3,1].
        av  = rmb.rjl(f, 0, 1, 3, 1)
        assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 03: pass')

    def test_hw07_prob03_ut04(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 04 ************')
        def f(x):
            return math.e**(-(x**2.0))
        err = 0.00001
        tv  = 0.7471804289095104
        ## Approximating integral of f(x) on [a=0, b=1] with R[2,2].
        av  = rmb.rjl(f, 0, 1, 2, 2)
        assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 04: pass')

    def test_hw07_prob03_ut06(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 06 ************')
        def f(x):
            return math.e**(-(x**2.0))
        err = 0.00001
        tv  = 0.7468241326473878
        ## Approximating integral of f(x) on [a=0, b=1] with R[5,4].
        av  = rmb.rjl(f, 0, 1, 5, 4)
        assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 06: pass')

    def test_hw07_prob03_ut07(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 07 ************')
        def f(x):
            return math.e**(-(x**2.0))
        err = 0.00001
        tv  = 0.7468241328124273
        ## Approximating integral of f(x) on [a=0, b=1] with R[10,10].
        av  = rmb.rjl(f, 0, 1, 10, 10)
        assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 07: pass')

    def test_hw07_prob03_ut08(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 08 ************')
        def f(x):
            return math.e**(-(x**2.0))
        err = 0.000001
        tv  = 0.7468241328124273
        ## Approximating integral of f(x) on [a=0, b=1] with R[20,20].
        av  = rmb.rjl(f, 0, 1, 25, 25)
        assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 08: pass')

    def test_hw07_prob03_ut09(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 09 ************')
        def f(t):
            return 2000*math.log(140000.0/(140000.0 - 2100*t), math.e) - 9.8*t
        err = 0.34
        tv  = 11061.0
        ## Approximating integral of f(x) on [a=8, b=30] with R[20,20].
        av  = rmb.rjl(f, 8, 30, 20, 20)
        assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 09: pass')

    def test_hw07_prob03_ut10(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 10 ************')
        ## f(x)
        def f(x):
            return 3.0*x**2.0 + 5.0*x
        ## anti-derivative of f(x)
        def antidf(x):
            return x**3.0 + 2.5*x**2.0
        err = 0.001
        tv  = antidf(10.0) - antidf(1.0)
        ## Approximating integral of f(x) on [a=1, b=10] with R[5,4].
        av  = rmb.rjl(f, 1, 10, 5, 4)
        #assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 10: pass')

    def test_hw07_prob03_ut11(self):
        print('\n***** CS3430: S22: HW07: Problem 03: Unit Test 11 ************')
        ## f(x)
        def f(x):
            return 3.0*x**2.0 + 5.0*x - 10.0
        ## anti-derivative of f(x)
        def antidf(x):
            return x**3.0 + 2.5*x**2.0 - 10.0*x
        err = 0.000001
        tv  = antidf(100.0) - antidf(51.0)
        ## Approximating integral of f(x) on [a=51, b=100] with R[15,14].
        av  = rmb.rjl(f, 51, 100, 15, 14)
        assert abs(tv - av) <= err
        print('av = {}'.format(av))
        print('tv = {}'.format(tv))
        print('CS 3430: S22: HW07: Problem 03: Unit Test 11: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
