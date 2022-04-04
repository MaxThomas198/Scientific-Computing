####################################
# module: cs3430_s22_hw04.py
# Maxwell Thomas
# A02215231
####################################

import numpy as np
#I couldn't figure out how to correctly do the second step of the pivot function so none of the tests pass
#2. Add the suitable multiples of the pivot’s row to the other rows in the
#tableau (including the p-row) to turn into 0’s all other entries in the
#pivot’s column.

### ============== Problem 1 ==================

def simplex(tab):
    """
    Apply the simplex algorithm to the tableau tab.
    """
    evc = find_evc(tab)
    dvr = find_dvr(tab, evc)
    if evc == -1:
        solution = (tab, True)
        return solution
    if evc != -1 and dvr == -1:
        nosolution = (tab, False)
        return nosolution
    else:
        simplex(pivot(dvr, evc, tab))


def pivot(dvr, evc, tab):
    in_vars, table = tab
    pivot = table[dvr][evc]
    #Rule 1
    table[dvr] = [element / pivot for element in table[dvr]]
    #Attempt at Rule 2 - This is where I mess up
    for index, row in enumerate(table):
        if index != dvr:
            row_scale = [y * table[index][evc]
                         for y in table[dvr]]
            table[index] = [x - y for x, y in
                                   zip(table[index],
                                       row_scale)]
    #Rule 3
    in_vars[dvr] = evc
    combo = (in_vars, table)
    return combo
def find_evc(tab):
    in_vars, table = tab
    lastrow = len(table[:, 0])
    m = min(table[lastrow - 1, :-1])
    if m <= 0:
        n = np.where(table[lastrow - 1, :-1] == m)[0][0]
    else:
        n = -1
    return n


def find_dvr(tab, evc):
    in_vars, table = tab
    rowlength = len(table[0, :]) - 1
    entercol = table[:, evc]
    endcol = table[:, rowlength]
    small = endcol[0] / entercol[0]
    checker = 100000
    dvr = -1
    for i in range(len(entercol) - 1):
        if endcol[i] != 0:
            checker = endcol[i] / entercol[i]
        if checker <= small:
            small = checker
            dvr = i
    return dvr


def get_solution_from_tab(tab):
    in_vars, mat = tab[0], tab[1]
    nr, nc = mat.shape
    sol = {}
    for k, v in in_vars.items():
        sol[v] = mat[k, nc - 1]
    sol['p'] = mat[nr - 1, nc - 1]
    return sol


def display_solution_from_tab(tab):
    sol = get_solution_from_tab(tab)
    for var, val in sol.items():
        if var == 'p':
            print('p\t=\t{}'.format(val))
        else:
            print('x{}\t=\t{}'.format(var, val))


### =============== Problem 2 ====================

def problem_2_1():
    ### replace tab with your definitions
    ### for Problem 2.1
    in_vars = {0: 2, 1: 3}
    m = np.array([[3, 8, 1, 0, 24],
                  [6, 4, 0, 1, 30],
                  [-2, -3, 0, 0, 0]],
                 dtype=float)
    tab = (in_vars, m)
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)


def problem_2_2():
    ### replace tab with your definitions
    ### for Problem 2.2.
    in_vars = {0: 2, 1: 3}
    m = np.array([[1, -1, 1, 0, 4],
                  [-1, 3, 0, 1, 4],
                  [-1, 0, 0, 0, 0]],
                 dtype=float)
    tab = (in_vars, m)
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)


def problem_2_3():
    ### replace tab with your definitions
    ### for Problem 2.3.
    in_vars = {0: 3, 1: 4, 2: 5}
    m = np.array([[12, 6, 0, 1, 0, 0, 1500],
                  [18, 12, 10, 0, 1, 0, 2500],
                  [0, 10, 0, 0, 0, 1, 2000],
                 [-1.5, -.8, -.25, 0, 0, 0, 0]],
                 dtype=float)
    tab = (in_vars, m)
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)


def problem_2_4():
    ### replace tab with your definitions
    ### for Problem 2.4.
    in_vars = {0: 3, 1: 4, 2: 5}
    m = np.array([[120, 80, 50, 1, 0, 1000],
                  [6, 4, 4, 0, 1, 600],
                  [-1, -1.2, -2, 0, 0, 0]],
                 dtype=float)
    tab = (in_vars, m)
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)
