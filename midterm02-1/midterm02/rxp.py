####################################
# module: rxp.py
# Maxwell Thomas
# A02215231
####################################

import numpy as np

class rxp(object):

    @staticmethod
    def drv1(f, cdd, x, h):
        return np.longdouble(cdd(f, x, h))

    @staticmethod
    def drv2(f, cdd, x, h):
        x1 = rxp.drv1(f, cdd, x, h/2.0)
        x2 = rxp.drv1(f, cdd, x, h)
        return  np.longdouble(x1 + (x1 - x2)/3.0)

    
    

    

    

    
        
    
