#############################################################
# module: cs3430_s22_midterm01.py
# Maxwell Thomas
# A02215231
##############################################################

### put your imports from your previous/current assignments
from cs3430_s22_hw02 import bsubst, fsubst, lud_solve
from cs3430_s22_hw01 import gje, cramer

### ================ Problem 01 ========================
def solve_lin_sys_with_bsubst(a, n, b, m):
    return bsubst(a, n, b, m)


### ================ Problem 02 ========================

def solve_lin_sys_with_fsubst(a, n, b, m):
    return fsubst(a, n, b, m)

### ================ Problem 03 ========================

def solve_lin_sys_with_gje(a, b):
    return gje(a, b)

### ================ Problem 04 ========================

def solve_lin_sys_with_lud(a, n, b, m):
    return lud_solve(a, n, b, m)

### ================ Problem 05 ========================

def solve_lin_sys_with_cramer(a, b):
    return cramer(a, b)

### ================ Problem 06 =========================

"""
1. Standard Maximization Problem (SMP) - Is a linear programming problem where we are looking for the maximum value of 
an object function. To be considered a SMP all variables have to be constrained to be non-negative, and every constraint 
is of the form: Linear function of the variables ≤ positive number.
2. Objective Function - This is the function we are trying to maximize, and we evaluate it at corner points to find
the maximum value.
3. Corner Point - A point on the boundary of the Feasible Set where every line segment contained in the set that
contains T has T as one of its end points.
4. Feasible Set - The Feasible Set is the set of points satisfying the constraints of the problem.
5. Two conditions when the simplex algorithm stops - The simplex algor. will stop if we can't find an entering variable
because all entries in the p-row are non-negative which means the algorithm has already found a solution. The other case
is when there is an entering variable, but there isn't a departing variable, which means that there is no solution.
6. Bounded Feasible Set - A F.S. is considered bounded when it needs to be contained within some circle centered at the
origin
7. Unbounded Feasible Set - If a F.S. is not contained within a boundary then it is considered unbounded.
"""

### ================ Problem 07 =========================

"""
Type your answer to Problem 07 here. Cleary state your
slack variables and the initial tableau.

Slack equations:
6x + z + u = 122        <- u is the slack variable
2y + 5z + v = 502       <- v is the slack variable
9x - 7y + 6z + w = 902  <- w is the slack variable

Initial tableau:
    x   y   z   u   v   w   B.S.
u   6   0   1   1   0   0   122
v   0   2   5   0   1   0   502
w   9   -7  6   0   0   1   902
p   -13 -7  -5  0   0   0   0

"""

### ================ Problem 08 =========================

"""
Type your answer to Problem 08 here. Cleary state how
you've identified the pivot, the pivot's location (row, column)
and its value.

The pivot is located at (1, 2) and its value is 6.
To find the pivot I first found the entering variable x1 which is the most negative entry in the p-row. Then I found the 
smallest ratio in the column which is 190/6 to find the departing variable of x3. 
"""

    
    
    
    






