import shutil
import argparse
import os
from cask.io.params import parameters
import cask.core.grid as grid
import cask.utilities.diagonalise_Hamiltonian as diagonalise_Hamiltonian


"""
cask main function that structures the code
"""
def main():

    # Current version of cask
    # Find a way to set this automatically from git...
    __version__=0.1

    # Parser class for cask
    parser = argparse.ArgumentParser(
        prog='cask',
        description='Planewave DFT',
        epilog='written by Nick Woods')

    # Specify arguments that cask can take
    parser.add_argument('--version', action='version', version='This is version {0} of cask.'.format(__version__))
    parser.add_argument('task', help='what do you want cask to do')

    args = parser.parse_args()

    # Default ground state energy computation

    # Read parameters into object params
    params = parameters()

    grid.G_vector_grid(params.cell,params.cut_off_energy)

    diagonalise_Hamiltonian.apply_Hartree()


    # Initialise (allocation, initialises wavefunctions, densities, etc.)i

    # Loop

    # diag_ham.py

    # Is the calculation converged?

    # density_mixing.py

    # Output: g.s. energy, density

