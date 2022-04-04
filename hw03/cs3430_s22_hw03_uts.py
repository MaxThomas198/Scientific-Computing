#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s22_hw03_uts.py
# description: unit tests for CS 3430: S22: Assignment 03
# bugs to vladimir kulyukin in canvas
##############################################################

import unittest
import numpy as np
from cs3430_s22_hw03 import line_ip, find_line_ips, max_obj_fun
from cs3430_s22_hw03 import plot_2_1_constraints, plot_2_2_constraints
from cs3430_s22_hw03 import plot_2_3_constraints
from cs3430_s22_hw03 import problem_2_1, problem_2_2
from cs3430_s22_hw03 import problem_2_3

class cs3430_s22_hw03_uts(unittest.TestCase):

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
    def check_line_ip(line1, line2, ip, err=0.0001):
        assert ip is not None
        A1, B1, C1 = line1
        A2, B2, C2 = line2
        x = ip[0, 0]
        y = ip[1, 0]
        print((A1 * x + B1 * y) - C1)
        print((A2 * x + B2 * y) - C2)
        assert abs((A1*x + B1*y) - C1) <= err
        assert abs((A2*x + B2*y) - C2) <= err
        return True
    
    @staticmethod
    def check_line_ip2(line1, line2, ip, err=0.0001):
        assert ip is not None        
        A1, B1, C1 = line1
        A2, B2, C2 = line2
        x = ip[0, 0]
        y = ip[1, 0]
        b1 = abs((A1*x + B1*y) - C1) <= err
        b2 = abs((A2*x + B2*y) - C2) <= err
        return b1 and b2
        
    ### ================ Problem 1: Unit Tests =====================
    
    def test_hw03_prob01_ut01(self):
        print('\n***** CS3430: S22: HW03: Problem 01: Unit Test 01 ************')

        #line1: 4x + 3y = 480
        line1 = (4.0, 3.0, 480.0)
        #line2: 3x + 6y = 720
        line2 = (3.0, 6.0, 720.0)
        ip12 = line_ip(line1, line2)
        print(ip12)
        cs3430_s22_hw03_uts.check_line_ip(line1, line2, ip12)

        #line3: 1x + 0y = 0
        line3 = (1, 0, 0)
        #line4: 0x + 1y = 0
        line4 = (0, 1, 0)
        ip12 = line_ip(line3, line4)
        print(ip12)
        cs3430_s22_hw03_uts.check_line_ip(line3, line4, ip12)

        ip13 = line_ip(line1, line3)
        print(ip13)
        cs3430_s22_hw03_uts.check_line_ip(line1, line3, ip13)

        ip31 = line_ip(line3, line1)
        print(ip31)
        cs3430_s22_hw03_uts.check_line_ip(line3, line1, ip31)

        ip14 = line_ip(line1, line4)
        print(ip14)
        cs3430_s22_hw03_uts.check_line_ip(line1, line4, ip14)

        ip41 = line_ip(line4, line1)
        print(ip41)
        cs3430_s22_hw03_uts.check_line_ip(line4, line1, ip41)

        ip23 = line_ip(line2, line3)
        print(ip23)
        cs3430_s22_hw03_uts.check_line_ip(line2, line3, ip23)

        ip32 = line_ip(line3, line2)
        print(ip32)
        cs3430_s22_hw03_uts.check_line_ip(line3, line2, ip32)

        ip24 = line_ip(line2, line4)
        print(ip24)
        cs3430_s22_hw03_uts.check_line_ip(line2, line4, ip24)

        ip42 = line_ip(line4, line2)
        print(ip42)
        cs3430_s22_hw03_uts.check_line_ip(line4, line2, ip42)

        print('CS 3430: S22: HW03: Problem 01: Unit Test 01: pass')

    def test_hw03_prob01_ut02(self):
        print('\n***** CS3430: S22: HW03: Problem 01: Unit Test 02 ************')
        line1 = (1,  0, 1)
        line2 = (1, -2, 0)
        line3 = (3,  4, 12)
        lines = [line1, line2, line3]
        ips = find_line_ips(lines)
        for i in range(len(lines)):
            ln1 = lines[i]
            for j in range(i+1, len(lines)):
                ln2 = lines[j]
                flag = False
                for ip in ips:
                    if cs3430_s22_hw03_uts.check_line_ip2(ln1, ln2, ip):
                        flag = True
                        print('found intersection point...')
                        break
                assert flag == True
        print(ips)
        print('CS 3430: S22: HW03: Problem 01: Unit Test 02: pass')

    def test_hw03_prob01_ut03(self):
        print('\n***** CS3430: S22: HW03: Problem 01: Unit Test 03 ************')

        line1 = (1,  1,  10)
        line2 = (1,  1, -10)        
        line3 = (2, -1,  10)
        line4 = (1, -3, -15)

        ip12 = line_ip(line1, line2)
        assert ip12 is None

        ip13 = line_ip(line1, line3)
        cs3430_s22_hw03_uts.check_line_ip(line1, line3, ip13)
        print(ip13)

        cps = find_line_ips([line1, line2, line3, line4])
        print(cps)
        print('CS 3430: S22: HW03: Problem 01: Unit Test 03: pass')

    def test_hw03_prob01_ut04(self):
        print('\n***** CS3430: S22: HW03: Problem 01: Unit Test 04 ************')        
        line1 = (1,  0, 1)
        line2 = (1, -2, 0)
        line3 = (3,  4, 12)
        ips = find_line_ips([line1, line2, line3])
        print(ips)
        f = lambda x, y: 10.0*x + 5.0*y
        err = 0.0001
        ip, v = max_obj_fun(f, ips)
        print(ip, v)
        assert abs(ip[0,0] - 2.4) <= err
        assert abs(ip[1,0] - 1.2) <= err
        assert abs(v - 30.0) <= err
        print('\n***** CS3430: S22: HW03: Problem 01: Unit Test 04 ************')

    def test_hw03_prob01_ut05(self):
        print('\n***** CS3430: S22: HW03: Problem 01: Unit Test 05 ************')
        red_line    = (4, 3, 480)
        blue_line   = (3, 6, 720)
        green_line  = (1, 0, 0)
        yellow_line = (0, 1, 0)
        ip1 = line_ip(green_line, yellow_line)
        ip2 = line_ip(green_line, blue_line)
        ip3 = line_ip(blue_line, red_line)
        ip4 = line_ip(red_line, yellow_line)
        obj_fun = lambda x, y: 5.0*x + 4.0*y
        ip, v = max_obj_fun(obj_fun, [ip1, ip2, ip3, ip4])        
        err = 0.0001
        assert abs(ip[0,0] - 48.0) <= err
        assert abs(ip[1,0] - 96.0) <= err
        assert abs(v - 624.0) <= err
        print('\n***** CS3430: S22: HW03: Problem 01: Unit Test 05 ************')

   ### ========================= Problem 02 ====================================        

    def test_hw03_prob02_ut01(self):
        print('\n***** CS3430: S22: HW03: Problem 02: Unit Test 01 ************')
        plot_2_1_constraints()
        x, y, p = problem_2_1()
        err = 0.0001
        assert abs(p - 13.0) <= err
        assert abs(x - 2.0) <= err
        assert abs(y - 7.0) <= err
        print('\n***** CS3430: S22: HW03: Problem 02: Unit Test 01 ************')

    def test_hw03_prob02_ut02(self):
        print('\n***** CS3430: S22: HW03: Problem 02: Unit Test 02 ************')
        plot_2_2_constraints()
        x, y, p = problem_2_2()
        err = 0.0001
        assert abs(p - 20.0/3.0) <= err        
        assert abs(x - 4.0/3.0) <= err
        assert abs(y - 16.0/3.0) <= err
        print('\n***** CS3430: S22: HW03: Problem 02: Unit Test 02 ************')

    def test_hw03_prob02_ut03(self):
        print('\n***** CS3430: S22: HW03: Problem 02: Unit Test 03 ************')
        plot_2_3_constraints()
        x, y, p = problem_2_3()
        print('x={}, y={}, p={}'.format(x, y, p))
        err = 0.0001
        assert abs(p - 650.0) <= err        
        assert abs(x - 100.0) <= err
        assert abs(y - 50.0) <= err
        print('\n***** CS3430: S22: HW03: Problem 02: Unit Test 03 ************')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
