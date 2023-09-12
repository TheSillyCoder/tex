import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as constants

L = 1

x = np.linspace(-L, L, 1000)

def b(n):
    return 4/((2*n - 1) * constants.pi)
def partial_sums(x, n):
    y = 0
    for i in range(1,n + 1):
        y += b(i)*np.sin(((2*i - 1)*constants.pi)*x/L)
    return y

fig, ax = plt.subplots(nrows = 2, ncols=2, figsize=(16,12), dpi=400)
fig.suptitle("Fourier Series")

n_s = [5, 10, 20, 40]

for i in [0, 1]:
    for j in [0, 1]:
        ax[i, j].set_title(f"{n_s[2*i + j]} terms")
        ax[i, j].axhline(0, color="black", lw=2)
        ax[i, j].axvline(0, color="black", lw=2)
        ax[i, j].set_ylim(-1.5, 1.5)
        ax[i, j].set_xticks([-L, 0, L], ["-L", "0", "L"])
        ax[i, j].step([-L, 0, L], [-1, -1, 1], "b", label="f(x)", lw=2)
        ax[i, j].plot(x, partial_sums(x, n_s[2*i + j]), "r", label=f"Fourier Series upto {n_s[2*i + j]} terms")
        ax[i, j].legend(loc="upper left")
plt.savefig("fourier_series_2.png", dpi=400)
plt.show()
