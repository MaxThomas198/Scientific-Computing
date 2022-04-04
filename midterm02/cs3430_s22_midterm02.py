###################################
## module: cs3430_s22_midterm02.py
## Maxwell Thomas
## A02215231
#####################################

import math
import numpy as np
import matplotlib.pyplot as plt
## YOUR IMPORTS
from rmb import rmb
from poly_parser import poly_parser
from tof import tof
from nra import nra
from drv import drv
## ========= Problem 1 ========================

def lambdify(s):
    return tof.tof(poly_parser.parse_sum(s))

## ========== Problem 2 ========================

def diff(s):
    return tof.tof(drv.drv(poly_parser.parse_sum(s)))

## ========== Problem 3 ========================

def nra_approx(s, x, num_iters=5):
    return nra.zr1(s, x, num_iters=5)

## ========== Problem 4 ========================

def cdd_drv1_ord2(f, x, h):
    return np.longdouble(((f(x + h) - f(x - h)) / (2 * h)))

def cdd_drv1_ord4(f, x, h):
    return np.longdouble((-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h))

def cdd_drv2_ord2(f, x, h):
    return np.longdouble((f(x + h) - 2*f(x) + f(x - h)) / np.square(h))

def cdd_drv2_ord4(f, x, h):
    return np.longdouble((-f(x + 2*h) + 16*f(x + h) - 30*f(x) + 16*f(x - h) - f(x - 2*h)) / (12*np.square(h)))

### ========= Problem 5 =========================

'''
Use this format to type-draw your solution.

          R(3,3)          -- Level 3
         /      \
    R(2,2)      R(3,2)    -- Level 2
    /    \     /    \
 T(1,1)   T(2,1)   T(3,1) -- Level 1

'''

## ========== Problem 6 ========================
def Sn(x, a_coeffs, b_coeffs):
    s = a_coeffs[0]/2
    for j in range(len(b_coeffs)):
        k = j + 1
        s += a_coeffs[k] * math.cos(k * x) + b_coeffs[j] * math.sin(k * x)
    return s


def plot_fourier_nth_partial_sum(f, fstr, num_points=10000, num_coeffs=3, rn=15):
    a, b = -math.pi, math.pi
    cos_coeffs = []
    sin_coeffs = []
    for k in range(num_coeffs + 1):
        fc = lambda x: f(x) * math.cos(k * x)
        ak = rmb.rjl(fc, a, b, rn, rn)/math.pi
        cos_coeffs.append(ak)
        if(k > 0):
            fs = lambda x: f(x) * math.sin(k * x)
            bk = rmb.rjl(fs, a, b, rn, rn)/math.pi
            sin_coeffs.append(bk)

    xvals = np.linspace(-math.pi, math.pi, num_points)
    yval1 = np.array([f(x) for x in xvals])
    yvals2 = np.array([Sn(x, cos_coeffs, sin_coeffs) for x in xvals])

    fig1 = plt.figure()
    fig1.suptitle('{}, num_coeffs = {}'.format(fstr, num_coeffs))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.plot(xvals, yval1, label=fstr, c='r')
    plt.plot(xvals, yvals2, label='Sn', c='b')
    plt.show()


def plot_fourier_nth_partial_sum_error(f, fstr, num_points=10000, num_coeffs=3, rn=15):
    a, b = -math.pi, math.pi
    cos_coeffs = []
    sin_coeffs = []
    for k in range(num_coeffs + 1):
        fs = lambda x: f(x) * math.cos(k * x)
        ak = rmb.rjl(fs, a, b, rn, rn) / math.pi
        cos_coeffs.append(ak)
        if (k > 0):
            fs = lambda x: f(x) * math.sin(k * x)
            bk = rmb.rjl(fs, a, b, rn, rn) / math.pi
            sin_coeffs.append(bk)

    xvals = np.linspace(-math.pi, math.pi, num_points)
    trueyvals = np.array([f(x) - Sn(x, cos_coeffs, sin_coeffs) for x in xvals])
    fig1 = plt.figure()
    fig1.suptitle('{}, num_coeffs = {}'.format(fstr, num_coeffs))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.plot(xvals, trueyvals, label='True Error', c='b')
    plt.show()

### =============== Problem 7 =========================

"""
Type your solution to Problem 7
"""

### =============== Problem 8 =========================

"""
Type your solution to Problem 8
"""

