#################################################
# module: cs3430_s22_hw03.py
# Maxwell Thomas
# A02215231
##################################################

import numpy as np
import matplotlib.pyplot as plt
from cs3430_s22_hw01 import gje


## =============== Problem 01 ==================

def line_ip(line1, line2):
    one = np.asarray(line1, dtype=float)
    two = np.asarray(line2, dtype=float)
    A = np.array([[one[0], one[1]],
                  [two[0], two[1]]])
    b = np.array([one[2], two[2]], dtype=float)
    ip = np.zeros((2, 1))
    det = float(np.linalg.det(A))
    if det == 0.0:
        return None
    else:
        x = gje(A, b)
        ip[0, 0] = x[0]
        ip[1, 0] = x[1]
        return ip


### This is the same as the static method
### cs3430_s22_hw03_uts.check_line_ip(line1, line2, ip, err=0.0001)
### in cs3430_s22_hw03_uts.py. This is for your
### convenience.
def check_line_ip(line1, line2, ip, err=0.0001):
    assert ip is not None
    A1, B1, C1 = line1
    A2, B2, C2 = line2
    x = ip[0, 0]
    y = ip[1, 0]

    assert abs((A1 * x + B1 * y) - C1) <= err
    assert abs((A2 * x + B2 * y) - C2) <= err
    return True


## Be careful not to compute the same intersection twice.
## In other words, if l1 and l2 are two lines, the
## intersection point b/w l1 and l2 is the same as the
## intersection point b/w l2 and l1. Computing duplicate
## intersections will not render the required computation
## incorrect, but it will make it more efficient.
def find_line_ips(lines):
    a = line_ip(lines[0], lines[1])
    b = line_ip(lines[1], lines[2])
    c = line_ip(lines[2], lines[0])
    ips = a, b, c
    return ips

## For problems 2.1 and 2.2
def max_obj_fun(f, cps):
    """
    maximize obj fun f on corner points cps
    """
    large = 0.0
    maximize = None
    for cp in cps:
        x = cp[0, 0]
        y = cp[1, 0]

        checker = f(x, y)
        if large < checker:
            large = checker
            farry = np.array([[x], [y]], dtype=float)
            maximize = (farry, f(x, y))

    return maximize


## =============== Problem 02 ==================

### Graphing constraints to the Ted's Toys problem we worked
### out in CS3430: S22: Lecture 05.
def plot_teds_constraints():
    ### plastic constraint: 4x + 3y <= 480
    def plastic_constraint(x): return -(4 / 3.0) * x + 160.0

    ### steel constraints: 3x + 6y <= 720
    def steel_constraint(x): return -0.5 * x + 120.0

    xvals = np.linspace(0, 160, 10000)
    yvals1 = np.array([plastic_constraint(x) for x in xvals])
    yvals2 = np.array([steel_constraint(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Ted\'s Toys Problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5, 160])
    plt.xlim([-5, 160])
    ## x = 0
    x1, y1 = [0, 0], [0, 160]
    ## y = 0
    x2, y2 = [0, 160], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='4x+3y=480', c='red')
    plt.plot(xvals, yvals2, label='3x+6y=720', c='blue')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()


def teds_problem():
    red_line = (4, 3, 480)
    blue_line = (3, 6, 720)
    green_line = (1, 0, 0)
    yellow_line = (0, 1, 0)

    cp1 = line_ip(green_line, yellow_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, yellow_line)

    obj_fun = lambda x, y: 5.0 * x + 4.0 * y

    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('num cars   = {}'.format(x))
    print('num trucks = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p


def plot_2_1_constraints():
    # 1.
    # x + y ≥ 3;
    # 2.
    # 3
    # x − y ≥ −1;
    # 3.
    # x ≤ 2.

    ### plastic constraint: 4x + 3y <= 480
    def plastic_constraint(x): return -(4 / 3.0) * x + 160.0

    ### steel constraints: 3x + 6y <= 720
    def steel_constraint(x): return -0.5 * x + 120.0

    xvals = np.linspace(0, 160, 10000)
    yvals1 = np.array([plastic_constraint(x) for x in xvals])
    yvals2 = np.array([steel_constraint(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Ted\'s Toys Problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5, 160])
    plt.xlim([-5, 160])
    ## x = 0
    x1, y1 = [0, 0], [0, 160]
    ## y = 0
    x2, y2 = [0, 160], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='4x+3y=480', c='red')
    plt.plot(xvals, yvals2, label='3x+6y=720', c='blue')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()


def problem_2_1():
    ### your code here
    pass


def plot_2_2_constraints():
    ### your code here
    pass


def problem_2_2():
    ### your code here
    pass


## For problem 2.3
def min_obj_fun(f, cps):
    """
    minimize obj fun f on corner points cps
    """
    ### your code here
    pass


def plot_2_3_constraints():
    ### your code here
    pass


def problem_2_3():
    ### your code here
    pass
