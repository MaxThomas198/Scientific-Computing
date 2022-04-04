
#############################################################
# module: cs3430_s22_midterm02_uts.py
# description: unit tests for CS3430: S22: Midterm 02
#############################################################

import unittest
import math
from cs3430_s22_midterm02 import *

class cs3430_s22_midterm02_uts(unittest.TestCase):

    ### ================ Problem 1: Unit Tests =====================

    def test_mid02_01(self):
        s1 = '1x^2 - 3x^0'
        f1 = lambdify(s1)
        gtf1 = lambda x: x**2 - 3
        for x in range(100):
            assert f1(x) == gtf1(x)

        s2 = '10x^5 + 4x^3 - 0.5x^2 - 0.25x^1 + 11x^0'
        f2 = lambdify(s2)
        gtf2 = lambda x: 10*(x**5) + 4*(x**3) - 0.5*(x**2) - 0.25*x + 11
        for x in range(100):
            assert f2(x) == gtf2(x)

        s3 = '-11x^0'
        f3 = lambdify(s3)
        gtf3 = lambda x: -11.0
        for x in range(100):
            assert f3(x) == gtf3(x)

        s4 = '5x^0'
        f4 = lambdify(s4)
        gtf4 = lambda x: 5.0
        for x in range(100):
            assert f4(x) == gtf4(x)

        s5 = '5x^-3 + 2x^-2 - 3x^-1 + 13x^0'
        f5 = lambdify(s5)
        gtf5 = lambda x: 5*(x**-3) + 2*(x**-2) - 3*(x**-1) + 13
        for x in range(1, 100):
            assert f5(x) == gtf5(x)        

        print('\ntest_mid02_01 passed...')


    ### ================ Problem 2: Unit Tests =====================

    def test_mid02_02(self):

        s1 = '1x^2 - 3x^1'
        f1 = diff(s1)
        gtf1 = lambda x: 2*x - 3
        for x in range(1, 100):
            assert f1(x) == gtf1(x)

        s2 = '10x^5 + 4x^3 - 0.5x^2 - 0.25x^1'
        f2 = diff(s2)
        gtf2 = lambda x: 50*(x**4) + 12*(x**2) - x - 0.25
        for x in range(1, 100):
            assert f2(x) == gtf2(x)

        s3 = '-11x^1'
        f3 = diff(s3)
        gtf3 = lambda x: -11.0
        for x in range(1, 100):
            assert f3(x) == gtf3(x)

        s4 = '5x^1'
        f4 = diff(s4)
        gtf4 = lambda x: 5.0
        for x in range(1, 100):
            assert f4(x) == gtf4(x)

        s5 = '5x^-3 + 2x^-2 - 3x^-1 + 13x^1'
        f5 = diff(s5)
        gtf5 = lambda x: -15*(x**-4) + -4*(x**-3) + 3*(x**-2) + 13
        for x in range(1, 100):
            assert f5(x) == gtf5(x)        
        
        print('\ntest_mid02_02 passed...')


    ### ================ Problem 3: Unit Tests =====================

    def test_mid02_03(self):
        err = 0.01
        s1 = '1x^3 - 1x^1 - 2.0x^0'        
        zr1 = nra_approx(s1, 1.0, num_iters=5)
        assert(abs(lambdify(s1)(zr1) - 0.0) <= err)
        print('\ntest_mid02_03 passed...')

        s2 = '4x^2 - 2x^2 + 3x^1'        
        zr2 = nra_approx(s2, 1.0, num_iters=5)
        assert(abs(lambdify(s2)(zr2) - 0.0) <= err)
        print('\ntest_mid02_03 passed...')

        s3 = '-5x^1'
        zr3 = nra_approx(s3, 1.0, num_iters=5)
        assert(abs(lambdify(s3)(zr3) - 0.0) <= err)

        s4 = '1x^3 - 2112x^1'        
        zr4 = nra_approx(s4, 1.0, num_iters=10)
        print(lambdify(s4)(zr4))
        assert(abs(lambdify(s4)(zr4) - 0.0) <= err)

        s5 = '1x^2 - 2x^0'
        zr5 = nra_approx(s5, 1.0, num_iters=10)
        assert(abs(math.sqrt(2) - zr5) <= err)

        s6 = '1x^3 - 7x^0'
        zr6 = nra_approx(s6, 1.0, num_iters=10)
        assert(abs((7**(1/3)) - zr6) <= err)

        s7 = '1x^5 - 8x^0'
        zr7 = nra_approx(s7, 1.0, num_iters=100)
        assert(abs((8**(1/5)) - zr7) <= err)

        print('\ntest_mid02_03 passed...')        

    ### ================ Problem 4: Unit Tests =====================
    
    def test_mid02_04(self):
        err = 0.001

        ### cdd_drv1_ord2
        f = lambda x: math.cos(x)
        x0, h = 0.765, 0.01
        av = cdd_drv1_ord2(f, x0, h)
        tv = -math.sin(x0)
        assert abs(av - tv) <= err

        f = lambda x: math.cos(x) + math.sin(x)
        x0, h = 0.931, 0.01
        av = cdd_drv1_ord2(f, x0, h)
        tv = -math.sin(x0) + math.cos(x0)
        assert abs(av - tv) <= err

        f = lambda x: -2*math.cos(x) + 3*math.sin(x)
        x0, h = 0.931, 0.01
        av = cdd_drv1_ord2(f, x0, h)
        tv = 2*math.sin(x0) + 3*math.cos(x0)
        print('abs={}'.format(abs(av-tv)))
        assert abs(av - tv) <= err

        ### cdd_drv1_ord4
        f = lambda x: math.cos(x)
        x0, h = 0.765, 0.01
        av = cdd_drv1_ord4(f, x0, h)
        tv = -math.sin(x0)
        assert abs(av - tv) <= err

        f = lambda x: math.cos(x) + math.sin(x)
        x0, h = 0.931, 0.01
        av = cdd_drv1_ord4(f, x0, h)
        tv = -math.sin(x0) + math.cos(x0)
        assert abs(av - tv) <= err

        f = lambda x: -2*math.cos(x) + 3*math.sin(x)
        x0, h = 0.931, 0.01
        av = cdd_drv1_ord4(f, x0, h)
        tv = 2*math.sin(x0) + 3*math.cos(x0)
        assert abs(av - tv) <= err

        ### cdd_drv2_ord4
        f = lambda x: math.cos(x)
        x0, h = 0.765, 0.01
        av = cdd_drv2_ord4(f, x0, h)
        tv = -math.cos(x0)
        assert abs(av - tv) <= err

        f = lambda x: math.cos(x) + math.sin(x)
        x0, h = 0.931, 0.01
        av = cdd_drv2_ord4(f, x0, h)
        tv = -math.cos(x0) - math.sin(x0)
        assert abs(av - tv) <= err

        f = lambda x: -2*math.cos(x) + 3*math.sin(x)
        x0, h = 0.931, 0.01
        av = cdd_drv2_ord4(f, x0, h)
        tv = 2*math.cos(x0) - 3*math.sin(x0)
        assert abs(av - tv) <= err

        ### cdd_drv2_ord4        
        f = lambda x: math.cos(x)
        x0, h = 0.765, 0.01
        av = cdd_drv2_ord4(f, x0, h)
        tv = -math.cos(x0)
        assert abs(av - tv) <= err

        f = lambda x: math.cos(x) + math.sin(x)
        x0, h = 0.931, 0.01
        av = cdd_drv2_ord4(f, x0, h)
        tv = -math.cos(x0) - math.sin(x0)
        assert abs(av - tv) <= err

        f = lambda x: -2*math.cos(x) + 3*math.sin(x)
        x0, h = 0.931, 0.01
        av = cdd_drv2_ord4(f, x0, h)
        tv = 2*math.cos(x0) - 3*math.sin(x0)
        assert abs(av - tv) <= err
        
        print('\ntest_mid02_04 passed...')


    ### ================ Problem 5: Unit Tests =====================
    ### No UTs

    ### ================ Problem 6: Unit Tests =====================
    
    def test_mid02_06(self):
        f = lambda x: 1
        fstr = 'y=1'
        plot_fourier_nth_partial_sum(f, fstr, num_points=10000, num_coeffs=3, rn=15)
        plot_fourier_nth_partial_sum_error(f, fstr, num_points=10000, num_coeffs=3, rn=15)

        f = lambda x: -(x**2)
        fstr = 'y=-x^2'
        plot_fourier_nth_partial_sum(f, fstr, num_points=10000, num_coeffs=100, rn=15)
        plot_fourier_nth_partial_sum_error(f, fstr, num_points=10000, num_coeffs=100, rn=15)

        f = lambda x: math.sqrt(13)
        fstr = 'y=sqrt(13)'
        plot_fourier_nth_partial_sum(f, fstr, num_points=10000, num_coeffs=10, rn=15)
        plot_fourier_nth_partial_sum_error(f, fstr, num_points=10000, num_coeffs=10, rn=15)

        f = lambda x: math.sin(x) + math.cos(x) + 2*(math.sin(2*x) + math.cos(2*x))
        fstr = 'y=sin(x)+cos(x)+2(sin(2x)+cos(2x))'
        plot_fourier_nth_partial_sum(f, fstr, num_points=10000, num_coeffs=10, rn=15)
        plot_fourier_nth_partial_sum_error(f, fstr, num_points=10000, num_coeffs=10, rn=15)

        print('\ntest_mid02_06 passed...')

    ### ================ Problem 7: Unit Tests =====================
    ### No UTs

    ### ================ Problem 8: Unit Tests =====================
    ### No UTs
        
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
