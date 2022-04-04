##################################################################
# module: cs3430_s22_hw08_uts.py
# description: unit tests CS3430: S22: HW08.
# YOUR NAME
# YOUR A#
# bugs to vladimir kulyukin via canvas
##################################################################

'''
Piany note frequences from https://en.wikipedia.org/wiki/Piano_key_frequencies

A7 - 3520.000
G7 - 3135.963 
E7 - 2637.020
D7 - 2349.318
----------

A6 - 1760.000
G6 - 1567.982 
E6 - 1318.510 
D6 - 1174.659
----------

A5 - 880.0000
G5 - 783.9909 
E5 - 659.2551
D5 - 587.3295
----------

A4 - 440 Hz
G4 - 391.9954 Hz
D4 - 293.6648 Hz
E4 - 329.6276 Hz
----------

A3 - 220.0000
G3 - 195.9977
E3 - 164.8138
D3 - 146.8324
----------

A2 - 110.0000
G2 - 97.99886
E2 - 82.40689
D2 - 73.41619
----------

A1 - 55.00000
G1 - 48.99943
E1 - 41.20344
D1 - 36.70810
----------
'''

import unittest
import math
import numpy as np
import matplotlib.pyplot as plt

from cs3430_s22_hw08 import nth_partial_sum_of_fourier_series
from cs3430_s22_hw08 import read_wavfile
from cs3430_s22_hw08 import recover_fourier_coeffs_in_range
from cs3430_s22_hw08 import plot_recovered_coeffs
from rmb import rmb

class cs3430_s22_hw08_uts(unittest.TestCase):

    ### ================= Problems 1 and 2 =======================

    def test_plot_fun_00(self, num_points=10000):
        """
        plots y = x^2 on [-pi, pi].
        """
        f = lambda x: x**2
        xvals = np.linspace(-math.pi, math.pi, num_points)
        yvals = np.array([f(x) for x in xvals])
        print('xvals = {}'.format(xvals[:5]))
        print('yvals = {}'.format(yvals[:5]))    
        fig1 = plt.figure(1)
        fig1.suptitle('y=x^2')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals, label='y=x^2', c='r')
        plt.legend(loc='best')
        plt.show()    

    def test_plot_fun_01(self, num_points=10000):
        """
        plots y = x^2 + 3 on [-pi, pi].
        """
        f = lambda x: x**2 + 3
        xvals = np.linspace(-math.pi, math.pi, num_points)
        yvals = np.array([f(x) for x in xvals])
        print('xvals = {}'.format(xvals[:5]))
        print('yvals = {}'.format(yvals[:5]))    
        fig1 = plt.figure(1)
        fig1.suptitle('y=x^2+3')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals, label='y=x^2+3', c='r')
        plt.legend(loc='best')
        plt.show()

    def test_plot_fun_02(self, num_points=10000):
        """
        plots y = 4x^2 -5 on [-pi, pi].
        """
        f = lambda x: 4*(x**2) - 5
        xvals = np.linspace(-math.pi, math.pi, num_points)
        yvals = np.array([f(x) for x in xvals])
        print('xvals = {}'.format(xvals[:5]))
        print('yvals = {}'.format(yvals[:5]))    
        fig1 = plt.figure(1)
        fig1.suptitle('y=4x^2-5')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals, label='y=4x^2-5', c='r')
        plt.legend(loc='best')
        plt.show()

    """
    test_nth_partial_sum_fun_00() shows that the Fourier series of f(x)=x^2 converges 
    to y=x^2 everywhere on [-pi, pi]; the coeffs in test_nth_partial_sum_00() are 
    computed with romberg(13,13); the 100-th partial sum of the series is computed 
    with these coefficients and then plotted against the values of f(x)=x^2 for 10000 
    values in [-pi, pi]. The plots are very similar and, when superimposed, should visually 
    form one curve.
    """
    def test_nth_partial_sum_fun_00(self, num_points=10000, num_coeffs=500):
        f = lambda x: x**2
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 13, 13)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=x^2; num_coeff={}'.format(num_coeffs))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=x^2', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
        plt.legend(loc='best')
        plt.show()
    
    def test_plot_error_fun_00(self, num_points=10000, num_coeffs=500):
        f = lambda x: x**2
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 13, 13)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=x^2; on [{}, {}]; num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        #plt.xlim([3.0, math.pi])
        plt.plot(xvals, err_vals, label='err', c='b')    
        plt.legend(loc='best')
        plt.show()


    ### ================= fun1: y = x^2 + 3 ============================
    """
    test_nth_partial_sum_fun_01() shows that the Fourier series of f(x)=x^2+3 converges 
    to y=x^2+3 everywhere on [-pi, pi]; the coeffs in test_nth_partial_sum_01() are 
    computed with romberg approximation; the partial sum of the series is computed 
    with these coefficients and then plotted against the values of f(x)=x^2+3 for 10000 
    values in [-pi, pi]. The plots are very similar and, when superimposed, should visually 
    form one curve.
    """
    def test_nth_partial_sum_fun_01(self, num_points=10000, num_coeffs=100):
        f = lambda x: x**2 + 3
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 13, 13)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=x^2+3; num_coeff={}'.format(num_coeffs))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=|x|', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
        plt.legend(loc='best')
        plt.show()

    def test_plot_error_fun_01(self, nsegs=1000, num_points=10000, num_coeffs=500):
        f = lambda x: x**2 + 3        
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 13, 13)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=x^2 + 3; on [{}, {}]; num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        plt.plot(xvals, err_vals, label='err', c='b')    
        plt.legend(loc='best')
        plt.show()


    ### ================= fun2: y = 4x^2 - 5 ============================

    """
    test_nth_partial_sum_fun_02() shows that the Fourier series of f(x)=4x^2+5 converges to y=4x^2-5 everywhere 
    on [-pi, pi]; the coeffs in test_nth_partial_sum_01() are computed with romberg approximation
    the partial sum of the series is computed with these coefficients and then
    plotted against the values of f(x)=4x^2-5 for 10000 values in [-pi, pi]. The plots are very
    similar and, when superimposed, should form one curve.
    """
    def test_nth_partial_sum_fun_02(self, num_points=10000, num_coeffs=200):
        f = lambda x: 4*(x**2) - 5
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 15, 15)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=4x^2-5; num_coeff={}'.format(num_coeffs))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=4x^2-5', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
        plt.legend(loc='best')
        plt.show()

    def test_plot_error_fun_02(self, nsegs=1000, num_points=10000, num_coeffs=200):
        f = lambda x: 4*(x**2) - 5        
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 13, 13)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=4x^2-5; on [{}, {}]; num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        #plt.xlim([3.0, math.pi])
        plt.plot(xvals, err_vals, label='err', c='b')    
        plt.legend(loc='best')
        plt.show()

    ### ============= Function 3:  y = x^4, ===========================

    """
    test_nth_partial_sum_fun_03() shows that the Fourier series of f(x)=x^4 converges to 
    y=x^4 everywhere 
    on [-pi, pi]; the coeffs in test_nth_partial_sum_01() are computed with romberg(13, 13)
    the partial sum of the series is computed with these coefficients and then
    plotted against the values of f(x)=x^4 for 10000 values in [-pi, pi]. The plots are very
    similar and, when superimposed, should form one curve.
    """
    def test_nth_partial_sum_fun_03(self, nsegs=1000, num_points=10000):
        f = lambda x: x**4
        n = 50
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(n):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 13, 13)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=x^4; num_coeff={}'.format(n))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=x^4', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
        plt.legend(loc='best')
        plt.show()

    ## |error| < 0.1, num_coeffs=900, romber(13,13). 
    def test_plot_error_fun_03(self, nsegs=1000, num_points=10000, num_coeffs=900):
        f = lambda x: x**4
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 13, 13)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=x^4; on [{}, {}]; num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        plt.plot(xvals, err_vals, label='err', c='b')    
        plt.legend(loc='best')
        plt.show()

    def test_nth_partial_sum_fun_04(self, nsegs=1000, num_points=10000):
        f = lambda x: -2*(x**4) + 1
        n = 50
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(n):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 13, 13)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=-2x^4+1; num_coeff={}'.format(n))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=-2x^4+1', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
        plt.legend(loc='best')
        plt.show()

    # The true error for this function is @ 0 from -1 through 1 and fluctuates between -.3 and .2 everywhere else.
    # The number of coefficients is num 900, and I used romber(13,13) like in the example.
    def test_plot_error_fun_04(self, nsegs=1000, num_points=10000, num_coeffs=900):
        f = lambda x: -2*(x**4) + 1
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals = [gtav[0] - gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=-2x^4+1; on [{}, {}]; num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        plt.plot(xvals, err_vals, label='err', c='b')
        plt.legend(loc='best')
        plt.show()

    def test_nth_partial_sum_fun_05(self, nsegs=1000, num_points=10000):
        f = lambda x: math.cos(x)
        n = 200
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(n):
            fc = lambda x: f(x)*math.cos(i*x)
            ai = rmb.rjl(fc, a, b, 13, 13)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x)*math.sin(i*x)
                bi = rmb.rjl(fs, a, b, 13, 13)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(a, b, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=cos(x) num_coeff={}'.format(n))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=cos(x)', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
        plt.legend(loc='best')
        plt.show()

    # The true error for this function is @ 0 around points -1.5 and 1.5.
    # The number of coefficients is num 900, and I used romber(13,13) like in the example.
    def test_plot_error_fun_05(self, nsegs=1000, num_points=10000, num_coeffs=900):
        f = lambda x: math.cos(x)
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals = [gtav[0] - gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=cos(x); on [{}, {}]; num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        plt.plot(xvals, err_vals, label='err', c='b')
        plt.legend(loc='best')
        plt.show()
        
    def test_nth_partial_sum_fun_06(self, nsegs=1000, num_points=10000):
        f = lambda x: math.cos(x) + 2*math.cos(2*x)
        n = 200
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(n):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(a, b, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=cos(x) + 2cos(2x) num_coeff={}'.format(n))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=cos(x) + 2cos(2x)', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')
        plt.legend(loc='best')
        plt.show()

    # The true error for this function is @ 0 around points -2.55, -.95, .95, and 2.55
    # The number of coefficients is num 400, and I used romber(13,13)
    def test_plot_error_fun_06(self, nsegs=1000, num_points=10000, num_coeffs=400):
        f = lambda x: math.cos(x) + 2*math.cos(2*x)
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals = [gtav[0] - gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=cos(x) + 2cos(2x); on [{}, {}]; num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        plt.plot(xvals, err_vals, label='err', c='b')
        plt.legend(loc='best')
        plt.show()

    def test_nth_partial_sum_fun_07(self, nsegs=1000, num_points=10000):
        f = lambda x: math.cos(x) + 2*math.cos(2*x) + 3*math.cos(3*x) + 4*math.cos(4*x) + 5*math.cos(5*x)
        n = 200
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(n):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(a, b, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=cos(x) + 2cos(2x) + 3cos(3x) + 4cos(4x) + 5cos(5x) num_coeff={}'.format(n))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=cos(x) + 2cos(2x) + 3cos(3x) + 4cos(4x) + 5cos(5x)', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')
        plt.legend(loc='best')
        plt.show()

    # The true error for this function is @ 0 around points -2.85, -2.3, -1.65, -1.1, -.5, .5, 1.1, 1.65, 2.3 and 2.85
    # The number of coefficients is num 200, and I used romber(13,13)
    def test_plot_error_fun_07(self, nsegs=1000, num_points=10000, num_coeffs=200):
        f = lambda x: math.cos(x) + 2*math.cos(2*x) + 3*math.cos(3*x) + 4*math.cos(4*x) + 5*math.cos(5*x)
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals = [gtav[0] - gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=cos(x) + 2cos(2x) + 3cos(3x) + 4cos(4x) + 5cos(5x); on [{}, {}]; '
                      'num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        plt.plot(xvals, err_vals, label='err', c='b')
        plt.legend(loc='best')
        plt.show()
        
    def test_nth_partial_sum_fun_08(self, nsegs=1000, num_points=10000):
        f = lambda x: abs(x)
        n = 200
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(n):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(a, b, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=|x| num_coeff={}'.format(n))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=|x|', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')
        plt.legend(loc='best')
        plt.show()

    # The true error for this function creates two triangles pointed at each other so the place with the smallest error
    # is right around 0.
    # The number of coefficients is num 900, and I used romber(13,13)
    def test_plot_error_fun_08(self, nsegs=1000, num_points=10000, num_coeffs=900):
        f = lambda x: abs(x)
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals = [gtav[0] - gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=|x|; on [{}, {}]; ' 'num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        plt.plot(xvals, err_vals, label='err', c='b')
        plt.legend(loc='best')
        plt.show()

    ### f9:  y = |x^5+3x+2|
    def test_nth_partial_sum_fun_09(self, nsegs=1000, num_points=10000):
        f = lambda x: abs(x**5 + 3*x + 2)
        n = 200
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(n):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(a, b, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=|x^5 + 3x + 2| num_coeff={}'.format(n))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=|x^5 + 3x + 2|', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')
        plt.legend(loc='best')
        plt.show()

    # The true error for this function is @ 0 from about -1.5 to about 1.5
    # The number of coefficients is num 900, and I used romber(13,13)
    def test_plot_error_fun_09(self, nsegs=1000, num_points=10000, num_coeffs=900):
        f = lambda x: abs(x**5 + 3*x + 2)
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals = [gtav[0] - gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=|x^5 + 3x + 2|; on [{}, {}]; ' 'num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        plt.plot(xvals, err_vals, label='err', c='b')
        plt.legend(loc='best')
        plt.show()

    ## f10: y = |sin(x)+2sin(2x)+3sin(3x)|
    def test_nth_partial_sum_fun_10(self, nsegs=1000, num_points=10000):
        f = lambda x: abs(math.sin(x) + 2*math.sin(2*x) + 3*math.sin(3*x))
        n = 200
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(n):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(a, b, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=|sin(x) + 2sin(2x) + 3sin(3x) num_coeff={}'.format(n))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.plot(xvals, yvals1, label='y=|sin(x) + 2sin(2x) + 3sin(3x)', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')
        plt.legend(loc='best')
        plt.show()

    # Where this function has the lowest error there are also lines adjacent, so I will list the points where the lines
    # are. -3.14, -2.2, -1.3, 0, 1.3, 2.2, 3.14
    # The number of coefficients is num 900, and I used romber(13,13)
    def test_plot_error_fun_10(self, nsegs=1000, num_points=10000, num_coeffs=900):
        f = lambda x: abs(math.sin(x) + 2*math.sin(2*x) + 3*math.sin(3*x))
        a, b = -math.pi, math.pi
        cos_coeffs = []
        sin_coeffs = []
        for i in range(num_coeffs):
            fc = lambda x: f(x) * math.cos(i * x)
            ai = rmb.rjl(fc, a, b, 13, 13) / math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fs = lambda x: f(x) * math.sin(i * x)
                bi = rmb.rjl(fs, a, b, 13, 13) / math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(-math.pi, math.pi, num_points)
        gt_vals = np.array([f(x) for x in xvals])
        approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
                                for x in xvals])
        err_vals = [gtav[0] - gtav[1] for gtav in zip(gt_vals, approx_vals)]
        fig1 = plt.figure(1)
        fig1.suptitle('True Error for y=|sin(x) + 2sin(2x) + 3sin(3x); on [{}, {}]; ' 
                      'num_coeffs={}'.format(a, b, num_coeffs))
        plt.xlabel('x')
        plt.ylabel('True Error')
        plt.grid()
        plt.plot(xvals, err_vals, label='err', c='b')
        plt.legend(loc='best')
        plt.show()
        
    ### =================== Problem 3 =======================

    def test_wavfile(self):
        fs, amps = read_wavfile('Guitar/Guitar_A_.wav')
        print('\nGuitar_A_.wav data:')
        print('frequency = {}'.format(fs))
        print('num amp readings = {}'.format(len(amps)))
        print(amps[:5])

        print('\nGuitar_D_.wav data:')
        fs, amps = read_wavfile('Guitar/Guitar_D_.wav')
        print('frequency = {}'.format(fs))
        print('num amp readings = {}'.format(len(amps)))
        print(amps[:5])

        print('\nGuitar_E.wav data:')
        fs, amps = read_wavfile('Guitar/Guitar_E_.wav')
        print('frequency = {}'.format(fs))
        print('num amp readings = {}'.format(len(amps)))
        print(amps[:5])

    def test_ut_02(self):
        ### recover A1 in Guitar_A_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Guitar_A_.wav', lower_k=53, upper_k=57)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_A', 'A1', lower_k=53, upper_k=57)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_A', 'A1', lower_k=53, upper_k=57)
        
        ### recover A7 - 3520.000 in Guitar_A_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Guitar_A_.wav', lower_k=3518, upper_k=3522)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_A', 'A7', lower_k=3518, upper_k=3522)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_A', 'A7', lower_k=3518, upper_k=3522)
        
        ### recover A1 in Guitar_D_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Guitar_D_.wav', lower_k=53, upper_k=57)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_D', 'A1', lower_k=53, upper_k=57)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_D', 'A1', lower_k=53, upper_k=57)
        
        ### recover A1 in Guitar_E_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Guitar_E_.wav', lower_k=53, upper_k=57)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_E', 'A1', lower_k=53, upper_k=57)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_E', 'A1', lower_k=53, upper_k=57)
        
        ### recover A1 in Guitar_G_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Guitar_G_.wav', lower_k=53, upper_k=57)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_G', 'A1', lower_k=53, upper_k=57)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_G', 'A1', lower_k=53, upper_k=57)
        
        ### recover D1 36.70810 in Guitar_D_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Guitar_D_.wav', lower_k=34, upper_k=38)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_D', 'D1', lower_k=34, upper_k=38)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_D', 'D1', lower_k=34, upper_k=38)
        
        ### recover D1 36.70810 in Guitar_A_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Guitar_A_.wav', lower_k=34, upper_k=38)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_A', 'D1', lower_k=34, upper_k=38)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_A', 'D1', lower_k=34, upper_k=38)
        
        ### recover D7 - 2349.318 in Guitar_D_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Guitar_D_.wav', lower_k=2347, upper_k=2351)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_D', 'D7', lower_k=2347, upper_k=2351)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Guitar_D', 'D7', lower_k=2347, upper_k=2351)

    def test_ut_03(self):
        ### recover A1 - 55.00000 in Violin_A_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_A_.wav', lower_k=53, upper_k=57)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A1', lower_k=53, upper_k=57)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A1', lower_k=53, upper_k=57)
        
        ### recover A2 - 110.0000 in Violin_A_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_A_.wav', lower_k=108, upper_k=112)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A2', lower_k=108, upper_k=112)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A2', lower_k=108, upper_k=112)
        
        ### recover A3 - 220.0000 in Violin_A_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_A_.wav', lower_k=218, upper_k=222)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A3', lower_k=218, upper_k=222)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A3', lower_k=218, upper_k=222)
        
        ### recover A4 - 440 Hz in Violin_A.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_A_.wav', lower_k=438, upper_k=442)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A4', lower_k=438, upper_k=442)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A4', lower_k=438, upper_k=442)
        
        ### recover A5 - 880.0000 in Violin_A.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_A_.wav', lower_k=878, upper_k=882)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A5', lower_k=878, upper_k=882)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A5', lower_k=878, upper_k=882)
        
        ### recover A6 - 1760.000 in Violin_A.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_A_.wav', lower_k=1758, upper_k=1762)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A6', lower_k=1758, upper_k=1762)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A6', lower_k=1758, upper_k=1762)
        
        ### recover A7 - 3520.000
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_A_.wav', lower_k=3518, upper_k=3522)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A7', lower_k=3518, upper_k=3522)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A', 'A7', lower_k=3518, upper_k=3522)

    def test_ut_04(self):
        ### recover G1 - 48.99943 in Violin_G_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_G_.wav', lower_k=47, upper_k=50)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G1', lower_k=47, upper_k=50)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G1', lower_k=47, upper_k=50)
        
        ### recover G2 - 97.99886 in Violin_G_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_G_.wav', lower_k=96, upper_k=99)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G2', lower_k=96, upper_k=99)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G2', lower_k=96, upper_k=99)
        
        ### recover G3 - 195.9977 in Violin_G_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_G_.wav', lower_k=194, upper_k=197)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G3', lower_k=194, upper_k=197)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G3', lower_k=194, upper_k=197)
        
        ### recover G4 - 391.9954 Hz in Violin_G.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_G_.wav', lower_k=390, upper_k=393)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G4', lower_k=390, upper_k=393)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G4', lower_k=390, upper_k=393)
        
        ### recover G5- 783.9909  in Violin_G.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_G_.wav', lower_k=782, upper_k=785)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G5', lower_k=782, upper_k=785)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G5', lower_k=782, upper_k=785)
        
        ### recover G6 - 1760.000 in Violin_G.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_G_.wav', lower_k=1758, upper_k=1762)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G6', lower_k=1758, upper_k=1762)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G6', lower_k=1758, upper_k=1762)
        
        ### recover G7 - 3135.963 in Violin_G.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_G_.wav', lower_k=3134, upper_k=3138)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G7', lower_k=3134, upper_k=3138)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_G', 'G7', lower_k=3134, upper_k=3138)

    def test_ut_05(self):
        ### recover E1 - 41.20344 in Violin_E_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=40, upper_k=42)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E1', lower_k=40, upper_k=42)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E1', lower_k=40, upper_k=42)
        
        ### recover E2 - 82.40689 in Violin_E_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=81, upper_k=84)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E2', lower_k=81, upper_k=84)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E2', lower_k=81, upper_k=84)
        
        ### recover E3 - 195.9977 in Violin_G_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_G_.wav', lower_k=194, upper_k=197)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E3', lower_k=194, upper_k=197)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E3', lower_k=194, upper_k=197)
        
        ### recover E4 - 329.6276 Hz in Violin_E.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=327, upper_k=332)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E4', lower_k=327, upper_k=332)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E4', lower_k=327, upper_k=332)
        
        ### recover E5 - 659.2551  in Violin_E.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=657, upper_k=661)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E5', lower_k=657, upper_k=661)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E5', lower_k=657, upper_k=661)
        
        ### recover E6 - 1318.510  in Violin_G.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=1317, upper_k=1320)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E6', lower_k=1317, upper_k=1320)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E6', lower_k=1317, upper_k=1320)
        
        ### recover E7 - 2637.020 in Violin_G.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=2636, upper_k=2639)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E7', lower_k=2636, upper_k=2639)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E7', lower_k=2636, upper_k=2639)

    ### A4 - 440 Hz
    ### G4 - 391.9954 Hz
    ### D4 - 293.6648 Hz
    ### E4 - 329.6276 Hz
    def test_ut_06(self):
        ### recover A4 - 440 in Violin_E_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=438, upper_k=442)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'A4', lower_k=438, upper_k=442)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'A4', lower_k=438, upper_k=442)
        
        ### recover G4 - 391.9954 Hz in Violin_E_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=389, upper_k=394)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'G4', lower_k=389, upper_k=394)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'G4', lower_k=389, upper_k=394)
        
        ### recover D4 - 293.6648 Hz in Violin_E_.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=292, upper_k=295)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'D4', lower_k=292, upper_k=295)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'D4', lower_k=292, upper_k=295)
        
        ### recover E4 - 329.6276 Hz in Violin_E.wav
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Violin/Violin_E_.wav', lower_k=328, upper_k=332)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E4', lower_k=328, upper_k=332)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_E', 'E4', lower_k=328, upper_k=332)

    ### A5 - 880.0000
    ### D5 - 587.3295 
    ### G5 - 783.9909 
    ### E5 - 659.2551
    def test_ut_07(self):
        ### recover A5 - 880 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav', lower_k=878, upper_k=882)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'A5',
                              lower_k=878, upper_k=882)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'A5',
                              lower_k=878, upper_k=882)
        
        ### recover D5 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav', lower_k=586, upper_k=589)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'D5',
                              lower_k=586, upper_k=589)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'D5',
                              lower_k=586, upper_k=589)
        
        ### recover G5 - 783.9909 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=782, upper_k=785)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'G5',
                              lower_k=782, upper_k=785)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'G5',
                              lower_k=782, upper_k=785)
        
        ### recover E5 - 659.2551 Hz in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=658, upper_k=661)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'E5',
                              lower_k=658, upper_k=661)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'E5',
                              lower_k=658, upper_k=661)


    ### A6 - 1760.000
    ### G6 - 1567.982 
    ### E6 - 1318.510 
    ### D6 - 1174.659        
    def test_ut_09(self):
        ### recover A6 - 1760.000 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=1758, upper_k=1762)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'A6',
                              lower_k=1758, upper_k=1762)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'A6',
                              lower_k=1758, upper_k=1762)
        
        ### recover G6 - 1567.982 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=1566, upper_k=1569)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'G6',
                              lower_k=1566, upper_k=1569)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'G6',
                              lower_k=1566, upper_k=1569)
        
        ### recover E6 - 1318.510  in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=1316, upper_k=1321)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'E6',
                              lower_k=1316, upper_k=1321)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'E6',
                              lower_k=1316, upper_k=1321)
        
        ### recover D6 - 1174.659 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=1173, upper_k=1176)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'D6',
                              lower_k=1173, upper_k=1176)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'D6',
                              lower_k=1173, upper_k=1176)

    ### A7 - 3520.000
    ### G7 - 3135.963 
    ### E7 - 2637.020
    ### D7 - 2349.318
    def test_ut_10(self):
        ### recover A7 - 3520.000 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=3518, upper_k=3522)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'A7',
                              lower_k=3518, upper_k=3522)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'A7',
                              lower_k=3518, upper_k=3522)
        
        ### recover G7 - 3135.963  in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=3133, upper_k=3137)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'G7',
                              lower_k=3133, upper_k=3137)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'G7',
                              lower_k=3133, upper_k=3137)
        
        ### recover E7 - 2637.020 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=2636, upper_k=2639)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'E7',
                              lower_k=2636, upper_k=2639)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'E7',
                              lower_k=2636, upper_k=2639)
        
        ### recover D7 - 2349.318 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_1_.wav',
                                                           lower_k=2347, upper_k=2352)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'D7',
                              lower_k=2347, upper_k=2352)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1', 'D7',
                              lower_k=2347, upper_k=2352)
    
    ### A7 - 3520.000
    ### G7 - 3135.963 
    ### E7 - 2637.020
    ### D7 - 2349.318
    ### discover and plot how much of each of the above notes is present in Beautiful_Gypsy_Lick_2_.wav.
    ### Plots 1 and 2 strongly suggest A7 is present. Plots 3 and 4 strongly suggest G7 is present. Plots 5 and 6
    ### suggest E7 is present. Plots 7 and 8 suggest D7 is present.
    def test_ut_11(self):
        ### recover A7 - 3520.000 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_2_.wav',
                                                           lower_k=3518, upper_k=3522)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2', 'A7',
                              lower_k=3518, upper_k=3522)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2', 'A7',
                              lower_k=3518, upper_k=3522)

        ### recover G7 - 3135.963  in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_2_.wav',
                                                           lower_k=3133, upper_k=3137)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2', 'G7',
                              lower_k=3133, upper_k=3137)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2', 'G7',
                              lower_k=3133, upper_k=3137)

        ### recover E7 - 2637.020 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_2_.wav',
                                                           lower_k=2636, upper_k=2639)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2', 'E7',
                              lower_k=2636, upper_k=2639)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2', 'E7',
                              lower_k=2636, upper_k=2639)

        ### recover D7 - 2349.318 in Beautiful_Gypsy_Lick_1
        acoeffs, bcoeffs = recover_fourier_coeffs_in_range('Guitar/Beautiful_Gypsy_Lick_2_.wav',
                                                           lower_k=2347, upper_k=2352)
        plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2', 'D7',
                              lower_k=2347, upper_k=2352)
        plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2', 'D7',
                              lower_k=2347, upper_k=2352)
            
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
