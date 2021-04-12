import numpy as np

m0 = 9.10938356e-31 #kg
e0 = 1.60217662e-19 #As
hbar = 6.626070040e-34 #Js

def Schroedinger(V, dx=1.0, meff=1, normalize=False):
	dx = dx * 1.0e-9
	N=len(V)
	
	#check if meff is scalar or vector
	if not hasattr(meff, "__len__"):
		meff = np.ones(N)*meff
	
	#effective electron mass
	_m=m0*meff

	mV = np.min(V)
	
	V = V-mV

	V = V

	#building hamiltonian
	fac =(hbar**2)/(2*_m*dx**2*e0)
	H0 = np.diag(2*fac*np.ones(N))-np.diag(fac[:-1]*np.ones(N-1), -1)-np.diag(fac[1:]*np.ones(N-1), 1)

	_V = np.diag(V)
	
	H = H0 + _V

	#calculating eigenstates and eigenenergies
	E, vecs = np.linalg.eigh(H)

	if normalize:
		for i in range(vecs.shape[0]):
			A = np.trapz(np.abs(vecs[:,i])**2, np.linspace(0, dx*N, N))
			vecs[:,i] = vecs[:,i] / np.sqrt(A)
	
	return (E+mV), vecs.T
	
if __name__ == "__main__":
	#Testing against an analytical model
	import matplotlib.pyplot as plt

	x = np.linspace(0,100,1000)
	V = np.ones_like(x)*2

	V[400:600]=V[400:600]-50000
	V = V-np.min(V)
	#V[200:300] = V[200:300]-0.45
	#V[700:800] = V[700:800]-0.45

	E, v = Schroedinger(V, dx=0.1, normalize=True)

	L = (600-400)*1e-10

	plt.plot(x,V)
	errors = []
	for i in range(5):
		Psi2 = np.abs(v[i])**2/1e9
		Psi2 = Psi2 - Psi2[0]
		plt.plot(x, Psi2+E[i])
		En = (i+1)**2 * np.pi**2 * hbar**2 / (2*m0*L**2)
		En = En / e0  + np.min(V)

		errors.append(np.abs(En-E[i]))

		plt.plot(x, np.ones_like(x)*En, ":")

	print("Mean Abs. Error: "+str(np.mean(errors)))
	plt.xlabel("z [nm]")
	plt.ylabel("E [eV]")
	plt.ylim([-0.1,1.1])
	plt.savefig("particle_in_box.png", dpi=80)
	plt.show()
