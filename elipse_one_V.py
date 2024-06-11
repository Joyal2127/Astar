import scipy.optimize as opt
import numpy as np

def ellipse_circumference_fixed_a(b, a=18):
    C = np.pi * (3 * (a + b) - np.sqrt((3 * a + b) * (a + 3 * b)))
    return C - 53

initial_guess_b = 5

b_solution = opt.fsolve(ellipse_circumference_fixed_a, initial_guess_b)

print(b_solution[0] if b_solution.size else "Solution not found")
