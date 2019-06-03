"""
Computes properties relating to the grid
"""

import numpy as np

# Calculate an array of allowed G vectors (plane-wave frequencies)
def G_vector_grid(cell,cut_off_energy):

    n, m, k = 0, 0, 0
    G_vectors = []

    # Triple loop over the POSITIVE REGION of the G vector sphere to find all G s.t. E(G) < E_cut and G.R = 2 pi (n,m,k)
    while m != 1:
        m = 0
        n = 0
        while n != 1:
            n = 0
            G_vector_energy = 0
            while G_vector_energy < cut_off_energy:
                # Compute G vector and associated energy for given (n,m,k)
                G_vector_current = np.ndarray.tolist(np.linalg.solve(cell, [2.0 * np.pi * n, 2.0 * np.pi * m, 2.0 * np.pi * k]))
                G_vectors.append(G_vector_current)
                G_vector_energy = 0.5 * np.linalg.norm(G_vector_current)**2
                n += 1

            # Remove final element of G vector list as we computed one too many
            G_vectors.pop()
            m += 1

        k += 1



#def real_space_grid():
#
    # Compute number of real space grid points in each direction

#def k_point_grid():
#
    # Define a MP k-point grid with a given spacing