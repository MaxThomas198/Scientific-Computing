#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s22_hw06_uts.py
# description: unit tests for CS 3430: S22: Assignment 06
#
# bugs to vladimir kulyukin on canvas
##############################################################

import unittest
from maker import maker
from poly_parser import poly_parser
from prod import prod
from const import const
from pwr import pwr
from var import var
from plus import plus
from tof import tof
from drv import drv
from nra import nra

class cs3430_s22_hw06_uts(unittest.TestCase):

    ### ================ Problem 1: Unit Tests =====================

    def test_hw06_prob01_ut01(self):
        print('\n***** CS3430: S22: HW06: Problem 01: Unit Test 01 ************')
        s1 = '5x^10'
        e1 = poly_parser.parse_elt(s1)
        err = 0.0001
        assert str(e1) == '(5.0*(x^10.0))'        
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert abs(e1.get_mult1().get_val() - 5.0) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() - 10.0) <= err
        print('CS 3430: S22: HW06: Problem 01: Unit Test 01: pass')

    def test_hw06_prob01_ut02(self):
        print('\n***** CS3430: S22: HW06: Problem 01: Unit Test 02 ************')
        s1 = '50.5123x^-123.345'
        e1 = poly_parser.parse_elt(s1)
        err = 0.0001
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert abs(e1.get_mult1().get_val() - 50.5123) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() + 123.345) <= err
        assert str(e1) == '(50.5123*(x^-123.345))'
        print('CS 3430: S22: HW06: Problem 01: Unit Test 02: pass')

    def test_hw06_prob01_ut03(self):
        print('\n***** CS3430: S22: HW06: Problem 01: Unit Test 03 ************')
        s1 = '-1001.7341y^-11.57'
        e1 = poly_parser.parse_elt(s1)
        err = 0.0001
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert abs(e1.get_mult1().get_val() + 1001.7341) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'y'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() + 11.57) <= err
        assert str(e1) == '(-1001.7341*(y^-11.57))'
        print('CS 3430: S22: HW06: Problem 01: Unit Test 03: pass')

    def test_hw06_prob01_ut04(self):
        print('\n***** CS3430: S22: HW06: Problem 01: Unit Test 04 ************')
        s1 = '1001.7341z^-11.57'
        e1 = poly_parser.parse_elt(s1)
        err = 0.0001
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert abs(e1.get_mult1().get_val() - 1001.7341) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'z'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() + 11.57) <= err
        assert str(e1) == '(1001.7341*(z^-11.57))'
        print('CS 3430: S22: HW06: Problem 01: Unit Test 04: pass')

    def test_hw06_prob01_ut05(self):
        print('\n***** CS3430: S22: HW06: Problem 01: Unit Test 05 ************')
        s1  = '5x^-10 + 3x^5'
        sum_ex  = poly_parser.parse_sum(s1)
        err = 0.0001
        assert isinstance(sum_ex, plus)
        assert isinstance(sum_ex.get_elt1(), prod)
        assert isinstance(sum_ex.get_elt2(), prod)
        e1 = sum_ex.get_elt1()
        assert abs(e1.get_mult1().get_val() - 5.0) <= err
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e1.get_mult2().get_deg().get_val() + 10.0) <= err
        assert str(e1) == '(5.0*(x^-10.0))'
        e2 = sum_ex.get_elt2()
        assert abs(e2.get_mult1().get_val() - 3.0) <= err
        assert isinstance(e2.get_mult2(), pwr)
        assert isinstance(e2.get_mult2().get_base(), var)
        assert e2.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert abs(e2.get_mult2().get_deg().get_val() - 5.0) <= err
        assert str(e2) == '(3.0*(x^5.0))'
        print('CS 3430: S22: HW06: Problem 01: Unit Test 05: pass')

    def test_hw06_prob01_ut06(self):
        print('\n***** CS3430: S22: HW06: Problem 01: Unit Test 06 ************')
        s1  = '5x^-10 + 3x^5 - 9x^3'
        sum_ex  = poly_parser.parse_sum(s1)
        err = 0.0001

        assert isinstance(sum_ex, plus)
        assert isinstance(sum_ex.get_elt1(), plus)
        assert isinstance(sum_ex.get_elt2(), prod)
        
        e1 = sum_ex.get_elt1() # e1 = 5x^-10 + 3x^5
        e2 = sum_ex.get_elt2() # e2 = -9x^3
        e11 = e1.get_elt1() # e11 = 5x^-10
        e12 = e1.get_elt2() # e12 = 3x^5 

        ## let's test e11 = 5x^-10
        assert abs(e11.get_mult1().get_val() - 5.0) <= err
        assert isinstance(e11.get_mult2(), pwr)
        assert isinstance(e11.get_mult2().get_base(), var)
        assert e11.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e11.get_mult2().get_deg(), const)
        assert abs(e11.get_mult2().get_deg().get_val() + 10.0) <= err
        assert str(e11) == '(5.0*(x^-10.0))'

        ## let's test e12 = 3x^5 
        assert abs(e12.get_mult1().get_val() - 3.0) <= err
        assert isinstance(e12.get_mult2(), pwr)
        assert isinstance(e12.get_mult2().get_base(), var)
        assert e12.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e12.get_mult2().get_deg(), const)
        assert abs(e12.get_mult2().get_deg().get_val() - 5.0) <= err
        assert str(e12) == '(3.0*(x^5.0))'

        ## let's test e2 = -9x^3
        assert abs(e2.get_mult1().get_val() + 9.0) <= err
        assert isinstance(e2.get_mult2(), pwr)
        assert isinstance(e2.get_mult2().get_base(), var)
        assert e2.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e2.get_mult2().get_deg(), const)
        assert abs(e2.get_mult2().get_deg().get_val() - 3.0) <= err
        assert str(e2) == '(-9.0*(x^3.0))'

        print('CS 3430: S22: HW06: Problem 01: Unit Test 06: pass')

    ### ================ Problem 2: Unit Tests =====================

    def test_hw06_prob02_ut01(self):
        print('\n***** CS3430: S22: HW06: Problem 02: Unit Test 01 ************')
        ex = '5x^2'
        my_fun = tof.tof(poly_parser.parse_sum(ex))
        gt_fun = lambda x: 5.0*(x**2.0)
        err = 0.0001
        for x in range(-1000000, 1000000):
            assert abs(my_fun(x) - gt_fun(x)) <= err
        print('CS 3430: S22: HW06: Problem 02: Unit Test 01: pass')

    def test_hw06_prob02_ut02(self):
        print('\n***** CS3430: S22: HW06: Problem 02: Unit Test 02 ************')
        ex = '5x^2 - 3x^5'
        print(poly_parser.parse_sum(ex))
        my_fun = tof.tof(poly_parser.parse_sum(ex))
        gt_fun = lambda x: 5.0*(x**2.0) - 3.0*(x**5.0)
        err = 0.0001
        for x in range(-1000000, 1000000):
            assert abs(my_fun(x) - gt_fun(x)) <= err
        print('CS 3430: S22: HW06: Problem 02: Unit Test 02: pass')

    def test_hw06_prob02_ut03(self):
        print('\n***** CS3430: S22: HW06: Problem 02: Unit Test 03 ************')
        ex = '5x^-2 - 3x^5 + 4.5x^7.342'
        my_fun = tof.tof(poly_parser.parse_sum(ex))
        gt_fun = lambda x: 5.0*(x**-2.0) - 3.0*(x**5.0) + 4.5*(x**7.342)
        err = 0.0001
        for x in range(-1000000, 0):
            assert abs(my_fun(x) - gt_fun(x)) <= err
        for x in range(1, 1000000):
            assert abs(my_fun(x) - gt_fun(x)) <= err            
        print('CS 3430: S22: HW06: Problem 02: Unit Test 03: pass')

    def test_hw06_prob02_ut04(self):
        print('\n***** CS3430: S22: HW06: Problem 02: Unit Test 04 ************')
        ex = '5x^-2 - 3x^5 + 4.5x^7.342 + 50x^1 - 100x^0'
        my_fun = tof.tof(poly_parser.parse_sum(ex))
        gt_fun = lambda x: 5.0*(x**-2.0) - 3.0*(x**5.0) + 4.5*(x**7.342) + 50.0*x - 100.0
        err = 0.0001
        for x in range(-1000000, 0):
            assert abs(my_fun(x) - gt_fun(x)) <= err
        for x in range(1, 1000000):
            assert abs(my_fun(x) - gt_fun(x)) <= err            
        print('CS 3430: S22: HW06: Problem 02: Unit Test 04: pass')

    ### ================ Problem 3: Unit Tests =====================

    def test_hw06_prob03_ut01(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 01 ************')
        rslt = drv.drv_const(maker.make_const(1.0))
        err = 0.0001
        assert isinstance(rslt, const)
        assert abs(rslt.get_val() - 0.0) <= err
        rslt = drv.drv_const(maker.make_const(153.0))
        assert isinstance(rslt, const)
        assert abs(rslt.get_val() - 0.0) <= err        
        print('CS 3430: S22: HW06: Problem 03: Unit Test 01: pass')

    def test_hw06_prob03_ut02(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 02 ************')
        s = '1x^1'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(fr.get_mult2())
        print(drv.drv_pwr(fr.get_mult2()))
        gtf = lambda x: 1.0
        f = tof.tof(drv.drv_pwr(fr.get_mult2()))
        err = 0.0001
        for i in range(-100, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 02: pass')

    def test_hw06_prob03_ut03(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 03 ************')
        s = '1y^1'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv_prod(fr))
        gtf = lambda y: 1.0
        f = tof.tof(drv.drv_prod(fr))
        err = 0.0001
        for i in range(-100, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 03: pass')

    def test_hw06_prob03_ut04(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 04 ************')
        s = '1z^1'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv_prod(fr))
        gtf = lambda x: 1.0
        f = tof.tof(drv.drv_prod(fr))
        err = 0.0001
        for i in range(-100, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 04: pass')

    def test_hw06_prob03_ut05(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 05 ************')
        s = '5x^3'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv_prod(fr))
        gtf = lambda x: 15.0*x**2.0
        f = tof.tof(drv.drv_prod(fr))
        err = 0.0001
        for i in range(-100, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 05: pass')

    def test_hw06_prob03_ut06(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 06 ************')
        s = '10x^4'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv_prod(fr))
        gtf = lambda x: 40.0*x**3.0
        f = tof.tof(drv.drv_prod(fr))
        err = 0.0001
        for i in range(-100, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 06: pass')

    def test_hw06_prob03_ut07(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 07 ************')
        s = '1x^-1'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv_prod(fr))
        gtf = lambda x: -1.0*x**(-2.0)
        f = tof.tof(drv.drv_prod(fr))
        err = 0.0001
        for i in range(-100, 0):
            assert abs(gtf(i) - f(i)) <= err
        for i in range(1, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 07: pass')

    def test_hw06_prob03_ut08(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 08 ************')
        s = '-3x^-1'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv_prod(fr))
        gtf = lambda x: 3.0*x**-2.0
        f = tof.tof(drv.drv_prod(fr))
        err = 0.0001
        for i in range(-100, 0):
            assert abs(gtf(i) - f(i)) <= err
        for i in range(1, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 08: pass')

    def test_hw06_prob03_ut09(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 09 ************')
        s = '10x^-3'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv_prod(fr))
        gtf = lambda x: -30.0*x**-4.0
        f = tof.tof(drv.drv_prod(fr))
        err = 0.0001
        for i in range(-100, 0):
            assert abs(gtf(i) - f(i)) <= err
        for i in range(1, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 09: pass')

    def test_hw06_prob03_ut10(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 10 ************')
        s = '10x^0.5'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv_prod(fr))
        gtf = lambda x: 5.0*x**-0.5
        f = tof.tof(drv.drv_prod(fr))
        err = 0.0001
        for i in range(1, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 10: pass')

    def test_hw06_prob03_ut11(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 11 ************')
        s  = '5x^3 + 3x^4'        
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv(fr))
        gtf = lambda x: 15.0*x**2.0 + 12.0*x**3
        f = tof.tof(drv.drv_plus(fr))
        err = 0.0001
        for i in range(-100, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 11: pass')

    def test_hw06_prob03_ut12(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 12 ************')
        rslt = drv.drv(maker.make_const(1.0))
        err = 0.0001
        assert isinstance(rslt, const)
        assert abs(rslt.get_val() - 0.0) <= err
        rslt = drv.drv(maker.make_const(153.0))
        assert isinstance(rslt, const)
        assert abs(rslt.get_val() - 0.0) <= err        
        print('CS 3430: S22: HW06: Problem 03: Unit Test 12: pass')

    def test_hw06_prob03_ut13(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 13 ************')
        s = '1x^1'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv(fr))
        gtf = lambda x: 1.0
        f = tof.tof(drv.drv(fr))
        err = 0.0001
        for i in range(-100, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 13: pass')

    def test_hw06_prob03_ut14(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 14 ************')
        s = '5x^3'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv(fr))
        gtf = lambda x: 15.0*x**2.0
        f = tof.tof(drv.drv(fr))
        err = 0.0001
        for i in range(-100, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 14: pass')

    def test_hw06_prob03_ut15(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 15 ************')
        s = '-3x^-1'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv(fr))
        gtf = lambda x: 3.0*x**-2.0
        f = tof.tof(drv.drv_prod(fr))
        err = 0.0001
        for i in range(-100, 0):
            assert abs(gtf(i) - f(i)) <= err
        for i in range(1, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 15: pass')

    def test_hw06_prob03_ut16(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 16 ************')
        s = '10x^-3'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv(fr))
        gtf = lambda x: -30.0*x**-4.0
        f = tof.tof(drv.drv(fr))
        err = 0.0001
        for i in range(-100, 0):
            assert abs(gtf(i) - f(i)) <= err
        for i in range(1, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 16: pass')

    def test_hw06_prob03_ut17(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 17 ************')
        s = '10x^0.5'
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv(fr))
        gtf = lambda x: 5.0*x**-0.5
        f = tof.tof(drv.drv(fr))
        err = 0.0001
        for i in range(1, 101):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 17: pass')

    def test_hw06_prob03_ut18(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 18 ************')
        s = '5x^-10 + 3x^5 - 9x^3'                
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv(fr))
        gtf = lambda x: -50.0*x**-11.0 + 15.0*x**4.0 - 27.0*x**2
        f = tof.tof(drv.drv(fr))
        err = 0.0001
        for i in range(1, 21):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 18: pass')

    def test_hw06_prob03_ut19(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 19 ************')
        s = '5x^-2 - 3x^5 + 4.5x^7.342 + 50x^1 - 100x^0'                
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv(fr))
        gtf = lambda x: -10.0*x**-3.0 - 15.0*x**4.0 + (4.5*7.342)*x**6.342 + 50.0
        f = tof.tof(drv.drv(fr))
        err = 0.0001
        for i in range(1, 21):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 19: pass')

    def test_hw06_prob03_ut20(self):
        print('\n***** CS3430: S22: HW06: Problem 03: Unit Test 20 ************')
        s = '5x^2 - 3x^5 + 10x^3 - 11x^4 + 1x^1 - 50x^0'                
        fr = poly_parser.parse_sum(s)
        print(fr)
        print(drv.drv(fr))
        gtf = lambda x: 10.0*x - 15.0*x**4.0 + 30.0*x**2 - 44.0*x**3 + 1.0
        f = tof.tof(drv.drv(fr))
        err = 0.0001
        for i in range(1, 21):
            assert abs(gtf(i) - f(i)) <= err
        print('CS 3430: S22: HW06: Problem 03: Unit Test 20: pass')

    ### ================ Problem 4: Unit Tests =====================

    def test_hw06_prob04_ut01(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 01 ************')
        s = '1x^3 - 1x^1 - 2.0x^0'
        zr = nra.zr1(s, 1.0, num_iters=5)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 01: pass')

    def test_hw06_prob04_ut02(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 02 ************')
        s = '1x^3 - 1x^1 - 2x^0'        
        zr, ni = nra.zr2(s, 1.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 02: pass')

    def test_hw06_prob04_ut03(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 03 ************')
        s = '3x^2 - 1x^0'        
        zr = nra.zr1(s, 1.0, num_iters=10)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 03: pass')

    def test_hw06_prob04_ut04(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 04 ************')
        s = '3x^2 - 1x^0'        
        zr, ni = nra.zr2(s, 1.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 04: pass')

    def test_hw06_prob04_ut05(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 05 ************')
        s = '1x^2 - 2x^0'        
        zr = nra.zr1(s, 1.0, num_iters=10)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 05: pass')

    def test_hw06_prob04_ut06(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 06 ************')
        s = '1x^2 - 2x^0'        
        zr, ni = nra.zr2(s, 1.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 05: pass')

    def test_hw06_prob04_ut07(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 07 ************')
        s = '1x^2 - 3x^0'        
        zr = nra.zr1(s, 1.0, num_iters=10)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 07: pass')

    def test_hw06_prob04_ut08(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 08 ************')
        s = '1x^2 - 3x^0'        
        zr, ni = nra.zr2(s, 1.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 08: pass')

    def test_hw06_prob04_ut09(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 09 ************')
        s = '100x^4 - 2x^3 - 15x^2 - 45x^-50'
        zr = nra.zr1(s, 1.0, num_iters=10)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 09: pass')

    def test_hw06_prob04_ut10(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 10 ************')
        s = '100x^4 - 2x^3 - 15x^2 - 45x^-50'
        zr, ni = nra.zr2(s, 1.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 10: pass')

    def test_hw06_prob04_ut11(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 11 ************')
        s = '300x^7 - 6x^4 - 30x^3 + 45x^2 + 7x^1 + 10x^0'
        zr = nra.zr1(s, 5.0, num_iters=40)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 11: pass')

    def test_hw06_prob04_ut12(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 12 ************')
        s = '300x^7 - 6x^4 - 30x^3 + 45x^2 + 7x^1 + 10x^0'
        zr, ni = nra.zr2(s, 5.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 12: pass')

    def test_hw06_prob04_ut13(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 13 ************')
        s = '400x^5 - 6x^4 - 30x^3 + 45x^2 + 7x^1 + 10x^0'
        zr = nra.zr1(s, 2.0, num_iters=15)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 13: pass')

    def test_hw06_prob04_ut14(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 14 ************')
        s = '400x^5 - 6x^4 - 30x^3 + 45x^2 + 7x^1 + 10x^0'
        zr, ni = nra.zr2(s, 2.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 14: pass')

    def test_hw06_prob04_ut15(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 15 ************')
        s = '2x^1'
        zr = nra.zr1(s, 10.0, num_iters=5)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 15: pass')

    def test_hw06_prob04_ut16(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 16 ************')
        s = '2x^1'
        zr, ni = nra.zr2(s, 10.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 16: pass')

    def test_hw06_prob04_ut17(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 17 ************')
        s = '2x^3'
        zr = nra.zr1(s, 10.0, num_iters=20)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0000001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 17: pass')

    def test_hw06_prob04_ut18(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 18 ************')
        s = '2x^3'
        zr, ni = nra.zr2(s, 10.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0000001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 18: pass')

    def test_hw06_prob04_ut19(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 19 ************')
        s = '5x^7'
        zr = nra.zr1(s, 5.0, num_iters=30)
        print('zr={}'.format(zr))
        assert nra.check_zr(s, zr, err=0.0000001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 19: pass')

    def test_hw06_prob04_ut20(self):
        print('\n***** CS3430: S22: HW06: Problem 04: Unit Test 20 ************')
        s = '5x^7'
        zr, ni = nra.zr2(s, 10.0, delta=0.0001)
        print('zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(s, zr, err=0.0000001)
        print('CS 3430: S22: HW06: Problem 04: Unit Test 20: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
