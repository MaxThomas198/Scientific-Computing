
####################################
# module: cdd.py
# Maxwell Thomas
# A02215231
####################################

import numpy as np

class cdd(object):

    @staticmethod
    def drv1_ord2(f, x, h):
        return np.longdouble(((f(x + h) - f(x - h)) / (2*h)))

    @staticmethod
    def drv1_ord4(f, x, h):
        return np.longdouble((-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h))

    @staticmethod
    def drv2_ord2(f, x, h):
        return np.longdouble((f(x + h) - 2*f(x) + f(x - h)) / np.square(h))

    @staticmethod
    def drv2_ord4(f, x, h):
        return np.longdouble((-f(x + 2*h) + 16*f(x + h) - 30*f(x) + 16*f(x - h) - f(x - 2*h)) / (12*np.square(h)))

    

    

    

    
        
    
