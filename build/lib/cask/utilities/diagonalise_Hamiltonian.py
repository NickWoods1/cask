"""
Finds the occupied eigenfunctions and associated eigenvalues

Input: Density
Output: A set of eigenfunctions and eigenvalues for each k-point
"""

import numpy as np


#def davidson():

    #apply_H
    #Converge loop.






#def apply_Hamiltonian(wavefunction,density):

    #apply hartree
    #apply kinetic
    #apply xc
    #apply local PP
    #apply nonlocal xc



def apply_Hartree():#density,wavefunction):




    x = np.ones((3,3,3))
    #x_fft = np.fft.fftn(x, s=(5,5,5), axes=(0,1,2))
    x_fft = np.fft.fftnfreq(x)
    y = np.zeros((3,3,3))

    #z = np.multiply(x,y)

    k = np.array([[[5,3,2],[1,2,3],[3,2,1]],[[5,3,2],[1,2,3],[3,2,1]],[[5,3,2],[1,2,3],[3,2,1]]])

    z = np.multiply(x_fft,k)


    x_ifft = np.fft.ifftn(z)

    print(x_ifft)

    #density.append(x)
    #density.append(y)
    #density.append(z)
    #density.append(k)

    #density_a = np.asarray(density)

    #print(density_test)

    #print(density_test.ndim)
    #print(density_test.shape)

   # dfft = np.fft.fft(density_a,5,axis = -2)

   # print(dfft)

    #print(np.fft.fftn(density, s = (5,5,5), axes = (-3,-2,-1)))


    # Fourier transform the density to G-space
    #density_Fourier.charge = np.fft.fftn(density.charge)

    # Construct the product in G-space rho(G)/|G|^2
    #density_Fourier.charge = density_Fourier.charge / G_vectors[]


    # Back FT

    # Ans * wavefunction