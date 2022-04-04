
#############################################
# Module: nra.py
# Description: Newton-Raphson Algorithm
#############################################

import numpy as np
import math
from maker import maker
from pwr import pwr
from prod import prod
from var import var
from const import const
from plus import plus
from drv import drv
from poly_parser import poly_parser
from tof import tof
import re

class nra(object):

    @staticmethod
    def zr1(fstr, x0, num_iters=3):
        els = re.split('([a-zA-Z^])', fstr)
        if len(els) == 5:
            expr = tof.tof(poly_parser.parse_elt(fstr))
        else:
            expr = tof.tof(poly_parser.parse_sum(fstr))
        deriv_expr = (drv.drv(expr))

        for i in range(num_iters):
            x = x0.get_val() - (expr(x0.get_val()) / deriv_expr(x0.get_val()))
            x0 = const(x)
        return x0

    @staticmethod
    def zr2(fstr, x0, delta=0.0001):
        ## your code here
        pass

    @staticmethod
    def check_zr(fstr, zr, err=0.0001):
        return abs(tof.tof(poly_parser.parse_sum(fstr))(zr) - 0.0) <= err 