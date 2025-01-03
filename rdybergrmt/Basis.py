"""
Basis
=====
This module contains the basis of the lattice.

"""

def get_spin_basis(L):
    """
    Get the spin basis of the lattice with no symmetry.

    Parameters
    ----------
    L : int
        The length of the lattice.

    Returns
    -------
    basis : list
        The basis of the lattice.
    
    """
    basis = []
    for i in range(2**L):
        basis.append(i)
    return basis
