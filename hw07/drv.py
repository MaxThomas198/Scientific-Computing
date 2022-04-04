###############################################
# module: drv.py
# module: a simple differentiation engine
###############################################

import numpy as np
import math
from maker import maker
from pwr import pwr
from prod import prod
from var import var
from const import const
from plus import plus

class drv(object):

    @staticmethod
    def drv(expr):
        if isinstance(expr, const):
            return drv.drv_const(expr)
        elif isinstance(expr, pwr):
            return drv.drv_pwr(expr)
        elif isinstance(expr, prod):
            return drv.drv_prod(expr)
        elif isinstance(expr, plus):
            return drv.drv_plus(expr)
        else:
            raise Exception('drv:' + str(expr))

    @staticmethod
    def drv_const(expr):
        assert isinstance(expr, const)
        return const(val=0.0)

    @staticmethod
    def drv_pwr(expr):
        b = expr.get_base()
        d = expr.get_deg()
        assert (isinstance(b, pwr) and b.get_deg().get_val() == 1.0) or \
            (isinstance(b, var))
        assert isinstance(d, const)
        if isinstance(b, const):
            if isinstance(d, pwr):  # e^(x^1)
                return expr
            elif isinstance(d, prod):  # 85 *e^(-0.5 *t)    => 85 *-0.5 *e^(-0.5 *t)
                return prod(expr, drv.drv(d))
            # e^(2x)
            elif isinstance(d, plus):
                return prod(expr, drv.drv(d))
        if isinstance(b, var):
            if isinstance(d, const):
                return prod(d, pwr(b, const(d.get_val() - 1)))
            elif isinstance(d, plus):
                return prod(d, pwr(b, const(d.get_elt2() - 1)))
            else:
                raise Exception('pwr_deriv: case 1: ' + str(expr))
        if isinstance(b, pwr):  # think this is (x^2 (^3))
            if isinstance(d, const):
                return prod(b.get_base(), prod(b.get_deg(), const))
            elif isinstance(d, pwr):  # e^(x^1)
                return expr
            else:
                raise Exception('pwr_deriv: case 2: ' + str(expr))
        elif isinstance(b, plus):  # (4x+2)^3 => 3(4x+2)^2 *4
            if isinstance(d, const):
                return prod(prod(d, pwr(b, const(d.get_val() - 1))), drv.drv(b))
            else:
                raise Exception('pwr_deriv: case 3: ' + str(expr))
        elif isinstance(b, prod):  # (3x)^2 => (2*3*x)^(2-1)
            if isinstance(d, const):
                return pwr(prod(d, prod(b.get_mult1(), b.get_mult2())), const(d.get_val() - 1))
            else:
                raise Exception('pwr_deriv: case 4: ' + str(expr))
        else:
            raise Exception('power_deriv: case 6: ' + str(expr))

    @staticmethod
    def drv_prod(expr):
        m1 = expr.get_mult1()
        m2 = expr.get_mult2()
        print(m1)
        print(m2)
        print("product drv")
        pass

    @staticmethod
    def drv_plus(expr):
        if isinstance(expr.get_elt2(), const):
            return drv.drv(expr.get_elt1())
        else:
            return plus(drv.drv(expr.get_elt1()), drv.drv(expr.get_elt2()))

