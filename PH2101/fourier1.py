import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as constants

L = 4
H = 1
x = np.linspace(0, L, 1000)

def c(n):
    return (32*H / (3*n*n*np.pi*np.pi))*np.sin(n*np.pi / 4)
def partial_sums(x, n):
    y = 0
    for i in range(1,n + 1):
        y += c(i)*np.sin((i*constants.pi)*x/L)
    return y
def f(arr):
    y = []
    for x in arr:
        if 0 <= x <= L/4 :
            y.append(4*H*x / L)
        elif L/4 <= x <= L:
            y.append(4*H*(L-x) / (3*L))
    return np.array(y)

fig, ax = plt.subplots(nrows = 2, ncols=2, figsize=(16,12), dpi=400)
fig.suptitle("Fourier Representation of the given string configuration")

n_s = [5, 10, 20, 40]

for i in [0, 1]:
    for j in [0, 1]:
        ax[i, j].set_title(f"{n_s[2*i + j]} terms")
        ax[i, j].axhline(0, color="black", lw=2)
        ax[i, j].axvline(0, color="black", lw=2)
        ax[i, j].set_xticks([0, L/4, L], ["0", r"$\frac{L}{4}$", "L"])
        ax[i, j].plot(x, f(x), "b", label="f(x)", lw=2)
        ax[i, j].plot(x, partial_sums(x, n_s[2*i + j]), "r", label=f"Fourier Series upto {n_s[2*i + j]} terms")
        ax[i, j].legend(loc="upper right")
plt.savefig("fourier_series_1.png", dpi=400)
plt.show()
