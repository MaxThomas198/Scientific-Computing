#!/usr/bin/python

###########################################
# module: maker.py
# bugs to vladimir dot kulyukin in canvas
###########################################

from var import var
from pwr import pwr
from const import const
from plus import plus
from prod import prod

class maker(object):

    @staticmethod
    def make_var(var_name):
        assert isinstance(var_name, str)
        return var(name=var_name)

    @staticmethod
    def make_const(val):
        assert isinstance(val, int) or isinstance(val, float)
        return const(val=float(val))

    @staticmethod
    def make_pwr(var_name, d):
        assert isinstance(d, int) or isinstance(d, float)
        return pwr(base=maker.make_var(var_name),
                   deg=maker.make_const(d))

    @staticmethod
    def make_prod(mult_expr1, mult_expr2):
        return prod(mult1=mult_expr1, mult2=mult_expr2)

    @staticmethod
    def make_plus(elt_expr1, elt_expr2):
        return plus(elt1=elt_expr1, elt2=elt_expr2)



