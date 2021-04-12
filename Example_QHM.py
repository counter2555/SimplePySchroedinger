from Schroedinger import Schroedinger
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    dx = 0.1
    x = np.linspace(-2,2,500)
    V = x**2

    Es, Psis = Schroedinger(V, dx, normalize=True)

    plt.plot(x,V)
    for i in range(20):
	    plt.plot(x, np.abs(Psis[i])**2/1e9+Es[i])

    plt.xlabel("z [nm]")
    plt.ylabel("E [meV]")
    plt.savefig("QHM.png", dpi=150)
    plt.show()
