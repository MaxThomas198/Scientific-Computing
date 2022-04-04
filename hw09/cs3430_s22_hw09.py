#!/usr/bin/python
# -*- coding: utf-8 -*-

######################################
# module: cs3430_s22_hw09.py
# description: cs3430 s22 hw09
# YOUR NAME
# YOUR A#
# bugs to vladimir kulyukin in canvas
######################################

def make_equiv_class_mod_n(a, n):
    """
    make_equiv_class_mod_n(a, n) returns a generator object
    to generate [a]_n (i.e., the equivalence class of a modulo n).
    """
    assert n > 0
    def gen_equiv_class(k):
        kk = k
        while True:
            yield a + kk*n
            if kk == 0:
                kk += 1
            elif kk > 0:
                kk *= -1
            elif kk < 0:
                kk *= -1
                kk += 1
    return gen_equiv_class(0)

def xeuc(a,b):
    """
    extended euclid algo that returns g, x, y such 
    g = gcd(a,b) and g = ax + by.
    """
    prevx, x = 1, 0
    prevy, y = 0, 1
    aa, bb = a, b
    while bb != 0:
        q = aa // bb
        x, prevx = prevx - (q * x), x
        y, prevy = prevy - (q * y), y
        aa, bb = bb, aa % bb
    return aa, prevx, prevy

def mult_inv_mod_n(a, n):
    """
    compute the multiplicative inverse of a mod n.
    """
    g, x, y = xeuc(a, n)
    if g != 1:
        return None
    else:
        return make_equiv_class_mod_n(x, n)

def solve_cong(a, b, m, tmax=10):
    """
    solves the congruence ax <> b (mod m);
    returns at most tmax equivalence classes.
    """
    a = a % m
    b = b % m
    classes = list()
    g, x, y = xeuc(a, m)
    i = 0
    while i < min(g, tmax):
        if (b % g != 0):
            return None
        x0 = (x * (b // g)) % m
        classes.append(make_equiv_class_mod_n(x0, m))
        i += 1

    return classes