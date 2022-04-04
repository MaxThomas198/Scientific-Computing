#!/usr/bin/python

#################################################
# module: tof.py
# bugs to vladimir kulyukin in canvas.
#################################################

from maker import maker
from var import var
from pwr import pwr
from const import const
from plus import plus
from prod import prod
import math

class tof(object):

    @staticmethod
    def const_tof(fr):
        """convert a const object to Py function."""
        assert isinstance(fr, const)

        def f(x):
            return fr.get_val()

        return f

    @staticmethod
    def var_tof(fr):
        """convert a var object to Py function."""        
        assert isinstance(fr, var)

        def f(x):
            return fr.get_name()

        return f

    @staticmethod
    def prod_tof(fr):
        """convert a prod object to Py function."""                
        assert isinstance(fr, prod)
        f1 = fr.get_mult1()
        f2 = fr.get_mult2()

        if isinstance(f1, var) and not isinstance(f2, var):
            def f(x):
                return x * tof.tof(f2)

            return f
        elif isinstance(f1, var) and isinstance(f2, var):
            def f(x):
                return x * x

            return f
        elif not isinstance(f1, var) and isinstance(f2, var):
            def f(x):
                return tof.tof(f2) * x

            return f
        else:
            def f(x):
                return tof.tof(f1)(x) * tof.tof(f2)(x)

            return f
    
    @staticmethod
    def plus_tof(fr):
        """convert a plus object to a Py function."""
        assert isinstance(fr, plus)
        f1 = fr.get_elt1()
        f2 = fr.get_elt2()
        print(f1)
        print(f2)
        if isinstance(f1, var) and not isinstance(f2, var):
            def f(x):
                return x + tof.tof(f2)(x)

            return f
        elif isinstance(f1, var) and isinstance(f2, var):
            def f(x):
                return x + x

            return f
        elif not isinstance(f1, var) and isinstance(f2, var):
            def f(x):
                return tof.tof(f1)(x) + x

            return f
        else:
            def f(x):
                return tof.tof(f1)(x) + tof.tof(f2)(x)
            return f

    @staticmethod
    def pwr_tof(fr):
        """convert a pwr object to a Py function."""
        assert isinstance(fr, pwr)
        f1 = fr.get_base()
        f2 = fr.get_deg()

        if isinstance(f1, var) and not isinstance(f2, var):
            def f(x):
                return math.pow(x, tof.tof(f2)(x))

            return f
        elif isinstance(f1, var) and isinstance(f2, var):
            def f(x):
                return math.pow(x, x)

            return f
        elif not isinstance(f1, var) and isinstance(f2, var):
            def f(x):
                return math.pow(tof.tof(f1)(x), x)

            return f
        else:
            def f(x):
                return math.pow(tof.tof(f1)(x), tof.tof(f2)(x))

            return f

    @staticmethod
    def tof(fr):
        """convert a const/var/prod/plus/pwr/ object to a Py function."""
        if isinstance(fr, const):
            return tof.const_tof(fr)
        elif isinstance(fr, var):
            return tof.var_tof(fr)
        elif isinstance(fr, prod):
            return tof.prod_tof(fr)
        elif isinstance(fr, plus):
            return tof.plus_tof(fr)
        elif isinstance(fr, pwr):
            return tof.pwr_tof(fr)
        else:
            raise Exception('tof: ' + str(fr))
    
