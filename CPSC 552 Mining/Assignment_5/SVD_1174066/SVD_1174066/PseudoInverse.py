import sys
import numpy as np
import matplotlib.pyplot as plt

def create_polynomial_data(x, poly_coeffs, add_noise):
    """
    Generate polynomial data with optional noise.
    """
    noise = np.random.normal(0, 2, len(x))
    y = poly_coeffs[0] * x**3 + poly_coeffs[1] * x**2 + poly_coeffs[2] * x + poly_coeffs[3]
    if add_noise:
        noisy_y = y + noise
    else:
        noisy_y = y
    return y, noisy_y

def plot_data(x, y, y2, yorig):
    """
    Plot original data, fitted data, and the original polynomial.

    """
    area = 10
    colors = ['black']
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, linewidths=8)
    plt.title('Pseudo Inverse - Linear Least Squares Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    line, = plt.plot(x, y, '-', linewidth=2, label="y-fitted")
    line.set_color('red')
    line, = plt.plot(x, y2, '-', linewidth=2, label="y-data")
    line.set_color('blue')
    line, = plt.plot(x, yorig, '--', linewidth=2, label="orig")
    line.set_color('green')
    plt.legend(loc="upper left")
    plt.show()

def solve_by_pseudo_inv(x, y, poly_order):
    """
    Solve for beta coefficients using pseudo-inverse.
    """
    A = np.zeros((len(x), poly_order + 1))
    for i in range(len(x)):
        for j in range(poly_order + 1):
            A[i, j] = x[i]**j
    u, s, vt = np.linalg.svd(A)
    s_inv = 1.0 / s
    sz = np.zeros(A.shape)
    sz[0:len(s), 0:len(s)] = np.diag(s_inv)
    sinv = sz
    pseudo_inv = np.dot(np.dot(vt.T, sinv.T), u.T)
    beta_coeffs = np.dot(pseudo_inv, y)
    return beta_coeffs

def main():
    x = np.asarray([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4], float)
    poly_coeffs = [2, -9, 8, 5]  # 2x^3 - 9x^2 + 8x + 5
    y, noisy_y = create_polynomial_data(x, poly_coeffs, True)
    plot_data(x, y, noisy_y, y)
    beta_coeffs = solve_by_pseudo_inv(x, noisy_y, 3)
    print('---------beta_coeffs--------')
    print(beta_coeffs)
    yfitted, noisy_y2 = create_polynomial_data(x, np.flip(beta_coeffs), False)
    plot_data(x, yfitted, noisy_y, y)

if __name__ == "__main__":
    sys.exit(int(main() or 0))
