#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s22_hw04_uts.py
# description: unit tests for CS 3430: S22: Assignment 04
# bugs to vladimir kulyukin in canvas
##############################################################

import unittest
import numpy as np
from cs3430_s22_hw04 import simplex
from cs3430_s22_hw04 import get_solution_from_tab
from cs3430_s22_hw04 import display_solution_from_tab
from cs3430_s22_hw04 import find_evc, find_dvr

class cs3430_s22_hw04_uts(unittest.TestCase):

    ### ================ Simplex Unit Tests =====================

    def test_simplex_ut01(self):
        print('\n***** CS3430: S22: HW04: Simplex Unit Test 01 ************')
        ## in vars
        in_vars = {0:3, 1:4}
        ## tableau
        m = np.array([[2,    2,   3, 1, 0, 160],
                      [5,    1,  10, 0, 1, 100],
                      [-10, -6,  -2, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        ## let's find the column of the entering variable (ev)
        evc = find_evc(tab)
        assert 0 == evc
        ## let's find the row of the departing variable (dv)
        assert 1 == find_dvr(tab, evc)
        ## print the new in vars
        print('in_vars = {}'.format(in_vars))
        print('tab = {}'.format(tab[1]))
        print('\n***** CS3430: S22: HW04: Simplex Unit Test 01 pass ************')        

    def test_simplex_ut02(self):
        print('\n***** CS3430: S22: HW04: Simplex Unit Test 02 ************')                        
        in_vars = {0:1, 1:0}
        m = np.array([[0, 8/5, -1, 1, -2/5, 120],
                      [1, 1/5,  2, 0, 1/5,  20],
                      [0, -4,  18, 0,  2,   200]],
                     dtype=float)
        tab = (in_vars, m)
        evc = find_evc(tab)
        assert 1 == evc
        assert 0 == find_dvr(tab, evc)
        print('in_vars = {}'.format(in_vars))
        print('tab = {}'.format(tab[1]))        
        print('\n***** CS3430: S22: HW04: Simplex Unit Test 02 pass ************')

    def test_simplex_ut03(self):
        print('\n***** CS3430: S22: HW04: Simplex Unit Test 03 ************')
        ## let's set up the in vars
        in_vars = {0:3, 1:4, 2:5}
        ## let's set up the initial tableau matrix
        m = np.array([[20,  4,  4, 1, 0, 0, 6000],
                      [8,   8,  4, 0, 1, 0, 10000],
                      [8,   4,  2, 0, 0, 1, 4000],
                      [-3, -8, -6, 0, 0, 0, 0]],
                     dtype=float)
        ## let's set up the tableau tuple of in vars and m.
        tab = (in_vars, m)
        ## apply the simplex
        tab, solved = simplex(tab)
        assert solved is True
        err = 0.0001
        ## get the solution from the tableau
        sol = get_solution_from_tab(tab)
        assert abs(sol[1] - 500.0) <= err
        assert abs(sol[2] - 1000.0) <= err        
        assert abs(sol[4] - 2000.0) <= err
        assert abs(sol['p'] - 10000.0) <= err
        ## display the in vars of the final tableau
        print('in_vars = {}'.format(in_vars))
        ## display the tableau matrix
        print('tab = {}'.format(tab[1]))
        ## display the solution
        print(sol)
        display_solution_from_tab(tab)
        print('\n***** CS3430: S22: HW04: Simplex Unit Test 03 pass ************')

    ### ================ Problem 1: Unit Tests =====================

    def test_hw04_prob01_ut01(self):
        print('\n***** CS3430: S22: HW04: Problem 01: Unit Test 01 ************')
        in_vars = {0:3, 1:4}
        m = np.array([[2,    2,   3, 1, 0, 160],
                      [5,    1,  10, 0, 1, 100],
                      [-10, -6,  -2, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        assert solved is True
        err = 0.0001
        sol = get_solution_from_tab(tab)
        assert abs(sol[0] - 5.0) <= err
        assert abs(sol[1] - 75.0) <= err
        assert abs(sol['p'] - 500.0) <= err        
        print('in_vars = {}'.format(in_vars))
        print('tab = {}'.format(tab[1]))
        print(get_solution_from_tab(tab))
        display_solution_from_tab(tab)
        print('\n***** CS3430: S22: HW04: Problem 01: Unit Test 01 pass ************')        

    def test_hw04_prob01_ut02(self):
        print('\n***** CS3430: S22: HW04: Problem 01: Unit Test 02 ************')
        in_vars = {0:3, 1:4, 2:5}
        m = np.array([[20,  4,  4, 1, 0, 0, 6000],
                      [8,   8,  4, 0, 1, 0, 10000],
                      [8,   4,  2, 0, 0, 1, 4000],
                      [-3, -8, -6, 0, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        assert solved is True
        err = 0.0001
        sol = get_solution_from_tab(tab)
        assert abs(sol[1] - 500.0) <= err
        assert abs(sol[2] - 1000.0) <= err        
        assert abs(sol[4] - 2000.0) <= err
        assert abs(sol['p'] - 10000.0) <= err
        print('in_vars = {}'.format(in_vars))
        print('tab = {}'.format(tab[1]))
        print(get_solution_from_tab(tab))
        display_solution_from_tab(tab)
        print('\n***** CS3430: S22: HW04: Problem 01: Unit Test 02 pass ************')        

    def test_hw04_prob01_ut03(self):
        print('\n***** CS3430: S22: HW04: Problem 01: Unit Test 03 ************')
        in_vars = {0:3, 1:4}
        m = np.array([[1,  -1,  1, 1, 0, 5],
                      [2,   0, -1, 0, 1, 10],
                      [-1, -2, -1, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        assert solved is False
        print('in_vars = {}'.format(in_vars))
        print('tab = {}'.format(tab[1]))
        print('\n***** CS3430: S22: HW04: Problem 01: Unit Test 03 pass ************')        

    def test_hw04_prob01_ut04(self):
        print('\n***** CS3430: S22: HW04: Problem 01: Unit Test 04 ************')
        in_vars = {0:2, 1:3}
        m = np.array([[ 4,  3,  1, 0, 480],
                      [ 3,  6,  0, 1, 720],
                      [-5, -4,  0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        err = 0.0001
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        sol = get_solution_from_tab(tab)
        assert abs(sol[0] - 48.0) <= err
        assert abs(sol[1] - 96.0) <= err
        assert abs(sol['p'] - 624.0) <= err
        print('in_vars = {}'.format(in_vars))
        print('tab = {}'.format(tab[1]))
        display_solution_from_tab(tab)
        print('\n***** CS3430: S22: HW04: Problem 01: Unit Test 04 pass ************')        

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
