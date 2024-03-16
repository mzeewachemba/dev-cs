import sys
from tkinter.tix import Tree
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import f

def create_polynomial_data(x, poly_coeffs, add_noise):
    ynoise = np.random.normal(0, 2, len(x))
    #print(ynoise)
    y = poly_coeffs[0] * x ** 4 + poly_coeffs[1] * x ** 3 + poly_coeffs[2] * x ** 2 + poly_coeffs[3] * x + poly_coeffs[4]   #4th order polynomial equation
    if add_noise == True:
        noisy_y = y + ynoise
    else:
        noisy_y = y
    return y, noisy_y

def plot_data(x, y, y2, yorig):
    area = 10
    colors = ['black']
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, linewidths=8)
    plt.title('Pseudo Inverse - Linear Least Squares Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    #plot the fitted line
    line, = plt.plot(x, y, '-', linewidth=2, label="y-fitted")
    line.set_color('red')
    line, = plt.plot(x, y2, '-', linewidth=2, label="y-data")
    line.set_color('blue')
    line, = plt.plot(x, yorig, '--', linewidth=2, label="orig")
    line.set_color('green')
    plt.legend(loc="upper left")
    plt.show()

def solve_by_Linear_Least_Squares(x, y, poly_order):
    A = np.zeros((poly_order+1, poly_order+1))
    b = np.zeros((poly_order+1))
    for i in range(0, poly_order+1):
        for j in range(0, poly_order+1):
            sum_val = 0
            for k in range(0, len(x)): # sum the data
                sum_val = sum_val + (x[k]**j)*(x[k]**i)
            A[i,j] = sum_val
    print(A)
    for i in range(0, poly_order+1):
        sumy = 0
        for k in range(0, len(x)): # sum the data
            sumy = sumy + y[k] * (x[k]**i)
        b[i] = sumy
    # compute inverse of A
    ainv = np.linalg.inv(A)

    beta_coeffs = np.dot(ainv,b) # multiply inverse of A with b
    print(f'beta_coefficients are: \n {beta_coeffs}')
    return beta_coeffs

def main():
    x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
    x = np.asarray(x, float)
    poly_coeffs = [2, -9, 8, 5 , 3]  # 2x^4 - 9x^3 + 8x^2 + 5x + 3  adding 4th coefficiant
    y, noisy_y = create_polynomial_data(x, poly_coeffs, True)
    # True means add noise, we are generating test data with noise
    # that has the starting polynomial of 2x^3 - 9x^2 + 8x + 5
    print(f'\nvalues of y are: \n {y}')
    plot_data(x, y, noisy_y, y)
    beta_coeffs = solve_by_Linear_Least_Squares(x, noisy_y, 4)
    print('---------beta_coeffs--------')
    print(beta_coeffs)
    # np.flip reverses the coefficient array
    yfitted, noisy_y2 = create_polynomial_data(x, np.flip(beta_coeffs), False) #
    # false means do not add noise
    plot_data(x, yfitted, noisy_y, y) # noisy_y was the data we fitted

if __name__ == "__main__":
    sys.exit(int(main() or 0))