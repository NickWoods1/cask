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



#def apply_Hartree(density,wavefunction):

    # Construct the product in G-space rho(G)/|G|^2
    # Fourier transform the density to G-space
    #density_Fourier.charge = np.fft.fftn(density.charge)

    # Construct the product in G-space rho(G)/|G|^2
    #while i < len():
        #while j < len():
            #while k < len():
                #v_hartree = 4 * np.pi * density_Fourier.charge[i,j,k] / np.linalg.norm(G_vectors[i,j,k])**2
                #i, j, k += 1, 1, 1

    # Back FT
    #v_hartree = np.fft.ifftn(v_hartree)

    # Hartree potential multiplied by the given trial wavefunction
    #v_hartree = np.multiply(v_hartree,wavefunction)

    # Return v_hartree