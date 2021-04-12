# SimplePySchroedinger
Simple python library for calculating the eigenstates of the schroedinger equation for a given potential distribution.

## Usage
The usage of this library is very simple. You only have to import the **Schroedinger** function from the **Schroedinger** module. The function takes the following arguments:

1. **V** - The potential well as a numpy array
1. **dx** - The spacing of the homogeneous grid in **nanometres**
1. **meff** - The effective mass (e.g. 0.065)
1. **normalize** - A boolean, which tells the function whether to normalize the wavefunctions

## Example: Quantum Harmonic Oscillator
A well known example of a potential well is the harmonic oscillator, which has a parabolic potential. One of the main properties of this potential is that the eigenenergies are equally spaced (ladder).

```python
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
```