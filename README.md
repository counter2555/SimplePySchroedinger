# SimplePySchroedinger
Simple python library for calculating the eigenstates of the schroedinger equation for a given potential distribution.

##Usage
The usage of this library is very simple. You only have to import the **Schroedinger** function from the **Schroedinger** module. The function takes the following arguments:

1. **V** - The potential well as a numpy array
1. **dx** - The spacing of the homogeneous grid in **nanometres**
1. **meff** - The effective mass (e.g. 0.065)
1. **normalize** - A boolean, which tells the function whether to normalize the wavefunctions

