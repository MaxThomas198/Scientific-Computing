#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################
# module: cs3430_s22_hw09_uts.py
# description: unit tests CS3430: S22: HW09.
# bugs to vladimir kulyukin in canvas.
##############################################

import unittest
import numpy as np
import random
from cs3430_s22_hw09 import xeuc
from cs3430_s22_hw09 import mult_inv_mod_n
from cs3430_s22_hw09 import solve_cong
from crt import crt

class cs3430_s22_uts(unittest.TestCase):

    ### ================= Problem 01 ============================

    def test_xeuc(self, num_tests=10000, lwr=1, uppr=100000):
        """
        Runs num_tests tests of xeuc by generating a and b
        randomly, where a, b are in [lwr, uppr], running xeuc(a,b)
        and checking if g = ax + by.
        """
        print('========= test_xeuc...')
        for i in range(num_tests):
            a = random.randint(lwr, uppr)
            b = random.randint(lwr, uppr)
            g, x, y = xeuc(a, b)
            print('{} = {}*{} + {}*{}'.format(g, a, x, b, y))
            assert g == a*x + b*y
            assert g > 0
            print('gcd({},{}) = {} = {}{} + {}{}'.format(a, b,
                                                         g, a, x, b, y))
        print('========= test_xeuc passed...')            

    ### ================= Problem 02 ============================
    
    def test_mult_inv_mod_n_01(self, num_tests=10):
        """
        tests example 1, slide 11, lecture 18.
        """
        print('========= test_mult_inv_mod_n_01...')
        a, n = 3, 10
        mi = mult_inv_mod_n(a, n)
        for _ in range(num_tests):
            x = next(mi)
            assert (a*x - 1) % n == 0
            print('\n{}*{}\t<>\t1\t(mod {})'.format(a, x, n))
        print('========= test_mult_inv_mod_n_01 passed...')            

    def test_mult_inv_mod_n_02(self, num_tests=10):
        """
        tests example 2, slide 11, lecture 18.
        """
        print('========= test_mult_inv_mod_n_02...')        
        a, n = 24, 19
        mi = mult_inv_mod_n(a, n)
        for _ in range(num_tests):
            x = next(mi)
            assert (a*x - 1) % n == 0
            print('\n{}*{}\t<>\t1\t(mod {})'.format(a, x, n))
        print('========= test_mult_inv_mod_n_02 passed...')                        

    def test_mult_inv_mod_n_03(self, num_tests=100, lwr=1, uppr=10000):
        """
        runs num_tests random tests of mult_inv_mod_n.
        """
        print('========= test_mult_inv_mod_n_03...')                
        for _ in range(num_tests):
            a = random.randint(lwr, uppr)
            n = random.randint(lwr, uppr)
            g, _, _ = xeuc(a, n)
            mi = mult_inv_mod_n(a, n)
            if g != 1:
                print('mi is None...')
                assert mi is None
            else:
                print('Testing equivalence class...')
                for _ in range(num_tests):
                    x = next(mi)
                    assert (a*x - 1) % n == 0
                print('Testing equivalence class done...')
        print('========= test_mult_inv_mod_n_03 passed...')                                
                    
    ### ================= Problem 03 ============================
    
    def test_solve_cong_01(self, num_tests=5):
        print('========= test_solve_cong_01...')                        
        a, b, m = 35, 10, 50
        equiv_classes = solve_cong(a, b, m)
        assert len(equiv_classes) == 5
        for i, ec in enumerate(equiv_classes):
            print('\nequivalence class {}'.format(i))
            for _ in range(num_tests):
                x = next(ec)
                assert (a*x - b) % m == 0
                print('{}*{}\t<>\t{}\t(mod {})'.format(a, x, b, m))
        print('========= test_solve_cong_01 passed...')                                        

    def test_solve_cong_02(self, num_tests=10, num_runs=2,
                                       lwr=1, uppr=10):
        print('========= test_solve_cong_02...')                                
        for _ in range(num_tests):
            a = random.randint(lwr, uppr)
            b = random.randint(lwr, uppr)
            m = random.randint(lwr+1, uppr)
            equiv_classes = solve_cong(a, b, m)
            if equiv_classes is None:
                print('\n{}*x\t<>\t{}\t(mod {}) has no solution'.format(a, b, m))
                continue
            g, _, _ = xeuc(a, m)
            print('\n{}*x\t<>\t{}\t(mod {}) has {} solution(s)'.format(a, b, m, g))
            for i, ec in enumerate(equiv_classes):
                print('\n\tequivalence class {}'.format(i))
                for _ in range(num_runs):
                    x = next(ec)
                    assert (a*x - b) % m == 0
                    print('\t{}*{}\t<>\t{}\t(mod {})'.format(a, x, b, m))
        print('========= test_solve_cong_02...')                                                    

    def test_solve_cong_03(self, num_tests=100, num_runs=2,
                                   lwr=1, uppr=100000):
        print('========= test_solve_cong_03...')                                        
        for _ in range(num_tests):
            a = random.randint(lwr, uppr)
            b = random.randint(lwr, uppr)
            m = random.randint(lwr+1, uppr)        
            equiv_classes = solve_cong(a, b, m)
            if equiv_classes is None:
                print('\n{}*x\t<>\t{}\t(mod {}) has no solution'.format(a, b, m))
                continue
            g, _, _ = xeuc(a, m)
            print('\n{}*x\t<>\t{}\t(mod {}) has {} solution(s)'.format(a, b, m, g))
            for i, ec in enumerate(equiv_classes):
                print('\n\tequivalence class {}'.format(i))
                for _ in range(num_runs):
                    x = next(ec)
                    assert (a*x - b) % m == 0
                    print('\t{}*{}\t<>\t{}\t(mod {})'.format(a, x, b, m))
        print('========= test_solve_cong_03 passed...')                                                            

    def test_solve_cong_04(self, num_tests=5):
        print('========= test_solve_cong_04...')                                                
        a, b, m = 35, 10, 2
        equiv_classes = solve_cong(a, b, m)
        assert len(equiv_classes) == 1
        for i, ec in enumerate(equiv_classes):
            print('\nequivalence class {}'.format(i))
            for _ in range(num_tests):
                x = next(ec)
                assert (a*x - b) % m == 0
                print('{}*{}\t<>\t{}\t(mod {})'.format(a, x, b, m))
        print('\ntest_solve_cong_04 passed...\n')

    def test_solve_cong_05(self, num_tests=5):
        print('\ntest_solve_cong_05...\n')
        a, b, m = 35, 10, 25
        equiv_classes = solve_cong(a, b, m)
        assert len(equiv_classes) == 5
        for i, ec in enumerate(equiv_classes):
            print('\nequivalence class {}'.format(i))
            for _ in range(num_tests):
                x = next(ec)
                assert (a*x - b) % m == 0
                print('{}*{}\t<>\t{}\t(mod {})'.format(a, x, b, m))
        print('\ntest_solve_cong_05 passed...\n')

    def test_solve_cong_06(self, num_tests=5):
        print('\ntest_solve_cong_06...\n')        
        a, b, m = 25, 1, 2
        equiv_classes = solve_cong(a, b, m)
        assert len(equiv_classes) == 1
        for i, ec in enumerate(equiv_classes):
            print('\nequivalence class {}'.format(i))
            for _ in range(num_tests):
                x = next(ec)
                assert (a*x - b) % m == 0
                print('{}*{}\t<>\t{}\t(mod {})'.format(a, x, b, m))
        print('\ntest_solve_cong_06 passed...\n')

    def test_solve_cong_07(self, num_tests=5):
        print('\ntest_solve_cong_07...\n')                
        a, b, m = 2, 1, 25
        equiv_classes = solve_cong(a, b, m)
        assert len(equiv_classes) == 1
        for i, ec in enumerate(equiv_classes):
            print('\nequivalence class {}'.format(i))
            for _ in range(num_tests):
                x = next(ec)
                assert (a*x - b) % m == 0
                print('{}*{}\t<>\t{}\t(mod {})'.format(a, x, b, m))
        print('\ntest_solve_cong_07 passed...\n')

    def test_solve_cong_08(self, num_tests=5):
        print('\ntest_solve_cong_08...\n')        
        a, b, m = 25, 8, 2
        equiv_classes = solve_cong(a, b, m)
        assert len(equiv_classes) == 1
        for i, ec in enumerate(equiv_classes):
            print('\nequivalence class {}'.format(i))
            for _ in range(num_tests):
                x = next(ec)
                assert (a*x - b) % m == 0
                print('{}*{}\t<>\t{}\t(mod {})'.format(a, x, b, m))
        print('\ntest_solve_cong_08 passed...\n')

    def test_solve_cong_09(self, num_tests=5):
        print('\ntest_solve_cong_09...\n')                
        a, b, m = 2, 1, 25
        equiv_classes = solve_cong(a, b, m)
        assert len(equiv_classes) == 1
        for i, ec in enumerate(equiv_classes):
            print('\nequivalence class {}'.format(i))
            for _ in range(num_tests):
                x = next(ec)
                assert (a*x - b) % m == 0
                print('{}*{}\t<>\t{}\t(mod {})'.format(a, x, b, m))
        print('\ntest_solve_cong_09 passed...\n')

    ### ================ Problem 04 =======================

    def test_crt_01(self):
        print('====== test_crt_01()...')
        mvals = [3, 4, 5]
        avals = [10, 11, 12]
        sols = crt.solve_congs(mvals, avals, num_sols=10)
        for x in sols:
            for a, m in zip(avals, mvals):
                assert (x - a) % m == 0
        for a, m in zip(avals, mvals):
            print('x <> {} = {}'.format(a, m))
        print(sols)
        print('====== test_crt_01() passed...')

    def test_crt_02(self, num_sols=5):
        print('====== test_crt_02()...')
        mvals  = [3, 4, 5]
        avals = [[1, 1, 1], [1, 1, 2], [1, 2, 1],
                 [2, 1, 1], [2, 2, 1], [2, 1, 2],
                 [1, 2, 2], [2, 2, 2]]
        for i, avls in enumerate(avals):
            sols = crt.solve_congs(mvals, avls, num_sols=3)
            for x in sols:
                for a, m in zip(avls, mvals):
                    assert (x - a) % m == 0
            print('\nSystem {}'.format(i+1))
            for a, m in zip(avls, mvals):
                print('x <> {} = {}'.format(a, m))
            print(sols)
        print('====== test_crt_02() passed...')            

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
